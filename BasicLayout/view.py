
#from pandas import DataFrame, Series
import pandas as pd
import numpy as np
from matplotlib import dates as mdates
from matplotlib import ticker as mticker
#from matplotlib.finance import candlestick_ohlc  #matplotlib2.0.0用
from mpl_finance import candlestick_ohlc #matplotlib3.0.0用
import matplotlib
import matplotlib.pyplot as plt
#from matplotlib.backends.backend_tkagg import FigureCanvasTk,NavigationToolbar2Tk  #matplotlib 2.0.2 
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)    ##matplotlib 3.0.2 
#matplotlib.use('TkAgg')  #只有matplotlib 2.0.2需要，高版本可不用设置
from matplotlib.figure import Figure
import datetime as dt
import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import Frame
from PIL import Image, ImageTk
import HP_global as g 
import HP_lib as mylib
import HP_draw as mydraw
import HP_data as hp
from  HP_draw import *

plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号

import matplotlib.ticker as ticker# 先设定一个日期转换方法
def format_date(x,pos=None): 
    # 由于前面股票数据在 date 这个位置传入的都是int 
    # 因此 x=0,1,2,... 
    # date_tickers 是所有日期的字符串形式列表 
    if x<0 or x>len(date_tickers)-1: 
        return '' 
    return date_tickers[int(x)]


#移动窗口到屏幕中央       
def setCenter(root,w,h):
    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()
    x = int( (ws/2) - (w/2) )
    y = int( (hs/2) - (h/2) )
    root.geometry('{}x{}+{}+{}'.format(w, h, x, y))

#移动窗口到屏幕坐标x,y       
def setPlace(root,x, y,w,h):
    root.geometry('{}x{}+{}+{}'.format(w, h, x, y))


#显示窗口ico图标
def showIco(root,Ico):
    root.iconbitmap(Ico)    

#是否禁止修改窗口大小
def reSizable(root,x,y):
    root.resizable(x, y)   #是否禁止修改窗口大小


def axview1(v,df,t,n=2):
    #显示K线,带6条均线
    df2=df.copy()
    # 生成横轴的刻度名字
    date_tickers=df2.date.values
    del df2['date']   
    df2['date']=df2.index
    ma5=pd.Series.rolling(df2.close, 5).mean()   #股票收盘价5日平均线 
    ma10=pd.Series.rolling(df2.close, 10).mean() #股票收盘价10日平均线 
    fig = plt.figure(facecolor=g.ubg,figsize=(1,1))
    ax=plt.subplot(fc=g.ubg)
    days = df2.reindex(columns=['date','open','high','low','close'])   

    def format_date(x,pos=None):
        if x<0 or x>len(date_tickers)-1:
            return ''
        return date_tickers[int(x)]

    ax.xaxis.set_major_locator(mticker.MaxNLocator(8))  #x轴分成几等分 
    ax.xaxis.set_major_formatter(ticker.FuncFormatter(format_date))  

    ax.tick_params(axis='y', colors=g.ufg)
    ax.tick_params(axis='x', colors=g.ufg)
    plt.ylabel('Stock price')
    candlestick_ohlc(ax, days.values, width=.6, colorup='#ff1717', colordown='#53c156')      
    ax.plot(days.date.values,ma5,label='MA5', linewidth=1.5)
    ax.plot(days.date.values,ma10,label='MA10', linewidth=1.5)
    if n>=3:
        ma20=pd.Series.rolling(df2.close, 20).mean() #股票收盘价20日平均线 
        ax.plot(days.date.values,ma20,label='MA20', linewidth=1.5)
    if n>=4:
        ma30=pd.Series.rolling(df2.close, 30).mean() #股票收盘价30日平均线 
        ax.plot(days.date.values,ma30,label='MA30', linewidth=1.5)
    if n>=5:
        ma60=pd.Series.rolling(df2.close, 60).mean() #股票收盘价60日平均线 
        ax.plot(days.date.values,ma60,label='MA60', linewidth=1.5)
    if n>=6:
        ma120=pd.Series.rolling(df2.close, 120).mean() #股票收盘价120日平均线 
        ax.plot(days.date.values,ma120,label='MA120', linewidth=1.5)    
    ax.grid(True, color='r')
    ax.xaxis.label.set_color(g.ufg)
    ax.yaxis.label.set_color(g.ufg)
    plt.legend() # 显示图中右上角的提示信息。
    plt.suptitle(t,color=g.ufg)
    plt.subplots_adjust(left=.06, bottom=.08, right=.96, top=.96, wspace=.15, hspace=0.1)
    plt.close() # 关窗口
    canvas =FigureCanvasTkAgg(fig, master=v)  # 设置tkinter绘图区
    canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=1)
    return ax

def axview1a(v,df,t):
    #无均线 K线图
    df2=df.copy()
    # 生成横轴的刻度名字
    date_tickers=df2.date.values
    del df2['date']   
    df2['date']=df2.index
    
    fig = plt.figure(facecolor=g.ubg,figsize=(1,1))
    ax=plt.subplot(fc=g.ubg)
    days = df2.reindex(columns=['date','open','high','low','close'])   
    def format_date(x,pos=None):
        if x<0 or x>len(date_tickers)-1:
            return ''
        return date_tickers[int(x)]

    ax.xaxis.set_major_locator(mticker.MaxNLocator(8))  #x轴分成几等分 
    ax.xaxis.set_major_formatter(ticker.FuncFormatter(format_date))      
    ax.tick_params(axis='y', colors=g.ufg)
    ax.tick_params(axis='x', colors=g.ufg)
    plt.ylabel('Stock price')
    candlestick_ohlc(ax, days.values, width=.6, colorup='#ff1717', colordown='#53c156')      
    ax.grid(True, color='r')
    ax.xaxis.label.set_color(g.ufg)
    ax.yaxis.label.set_color(g.ufg)
    plt.suptitle(t,color=g.ufg)
    plt.subplots_adjust(left=.06, bottom=.08, right=.96, top=.96, wspace=.15, hspace=0.1)
    plt.close() # 关窗口
    canvas =FigureCanvasTkAgg(fig, master=v)  # 设置tkinter绘图区
    canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=1)
    return ax

def axview1b(v,df,t):
    #叠加成交量的均线
    df2=df.copy()
    # 生成横轴的刻度名字
    date_tickers=df2.date.values
    del df2['date']   
    df2['date']=df2.index
    ma5=pd.Series.rolling(df2.close, 5).mean()   #股票收盘价5日平均线 
    ma20=pd.Series.rolling(df2.close, 20).mean() #股票收盘价20日平均线 
    fig = plt.figure(facecolor=g.ubg,figsize=(1,1))
    ax=plt.subplot(fc=g.ubg)
    days = df2.reindex(columns=['date','open','high','low','close'])   
    def format_date(x,pos=None):
        if x<0 or x>len(date_tickers)-1:
            return ''
        return date_tickers[int(x)]

    ax.xaxis.set_major_locator(mticker.MaxNLocator(8))  #x轴分成几等分 
    ax.xaxis.set_major_formatter(ticker.FuncFormatter(format_date))   
    ax.tick_params(axis='y', colors=g.ufg)
    ax.tick_params(axis='x', colors=g.ufg)
    plt.ylabel('Stock price')
    candlestick_ohlc(ax, days.values, width=.6, colorup='#ff1717', colordown='#53c156')      
    ax.plot(days.date.values,ma5,label='MA5', linewidth=1.5)
    ax.plot(days.date.values,ma20,label='MA20', linewidth=1.5)
    ax.grid(True, color='r')
    ax.xaxis.set_major_locator(mticker.MaxNLocator(8))  #x轴分成几等分 
    ax.xaxis.label.set_color(g.ufg)
    ax.yaxis.label.set_color(g.ufg)
    plt.legend() # 显示图中右上角的提示信息。
    plt.suptitle(t,color=g.ufg)
    
    ax0 = ax.twinx()
    ax0.tick_params(axis='y', colors=g.ufg)
    v1=mylib.G_MA(df2['volume'],g.MA1)
    v2=mylib.G_MA(df2['volume'],g.MA2)
    rsiCol = '#c1f9f7'
    posCol = '#386d13'
    ax0.plot(days.date.values, v1, rsiCol, linewidth=1,label="$MA5$", alpha=.5)
    ax0.plot(days.date.values, v2, posCol, linewidth=1,label="$MA10$", alpha=.5)
    ax0.bar(days.date.values,df2.volume.values, facecolor='#386d13', alpha=.5)
    ax0.yaxis.label.set_color(g.ufg)
    
    ax0.tick_params(axis='y', colors=g.ufg)
    ax0.tick_params(axis='x', colors=g.ufg)
    ax0.yaxis.set_major_locator(mticker.MaxNLocator(nbins=4, prune='upper'))
    ax0.tick_params(axis='x', colors=g.ufg)    
    
    plt.subplots_adjust(left=.06, bottom=.08, right=.96, top=.96, wspace=.15, hspace=0.1)
    plt.close() # 关窗口
    canvas =FigureCanvasTkAgg(fig, master=v)  # 设置tkinter绘图区
    canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=1)
    return ax

def axview1c(v,df,t):
    #叠加成交密度的K线
    df2=df.copy()
    dfmax=df2.close.max()
    dfmin=df2.close.min()
    l=len(df2)
    if l<80:
        l=int(l/2)
    else:
        l=40
        
    a=(dfmax-dfmin)/l
    x=dfmin
    mm=[]
    while x<=dfmax:
        mm.append(x)
        x+=a

    mma=pd.Series( mm,name='m')
    df4=mma.to_frame('p')
    df4['v']=0
    for i in df2.index:
        j=int((df2.close.loc[i]-dfmin)/a)
        if j>=l:
            j-=1
        df4.v.loc[j]=df4.v.loc[j]+df2.close.loc[i]

    # 生成横轴的刻度名字
    date_tickers=df2.date.values
    del df2['date']   
    df2['date']=df2.index
    ma5=pd.Series.rolling(df2.close, 5).mean()   #股票收盘价5日平均线 
    ma20=pd.Series.rolling(df2.close, 20).mean() #股票收盘价20日平均线 
    fig = plt.figure(facecolor=g.ubg,figsize=(1,1))
    ax=plt.subplot(fc=g.ubg)
    days = df2.reindex(columns=['date','open','high','low','close'])   
    def format_date(x,pos=None):
        if x<0 or x>len(date_tickers)-1:
            return ''
        return date_tickers[int(x)]

    ax.xaxis.set_major_locator(mticker.MaxNLocator(8))  #x轴分成几等分 
    ax.xaxis.set_major_formatter(ticker.FuncFormatter(format_date))  
    ax.tick_params(axis='y', colors=g.ufg)
    ax.tick_params(axis='x', colors=g.ufg)
    plt.ylabel('Stock price')
    candlestick_ohlc(ax, days.values, width=.6, colorup='#ff1717', colordown='#53c156')      
    ax.plot(days.date.values,ma5,label='MA5', linewidth=1.5)
    ax.plot(days.date.values,ma20,label='MA20', linewidth=1.5)
    ax.grid(True, color='r')
    ax.xaxis.set_major_locator(mticker.MaxNLocator(8))  #x轴分成几等分 
    ax.xaxis.label.set_color(g.ufg)
    ax.yaxis.label.set_color(g.ufg)
    plt.legend() # 显示图中右上角的提示信息。
    plt.suptitle(t,color=g.ufg)
   
    ax0 = ax.twiny()
    ax0.barh(df4.p,df4.v, height=0.05, align='center', color='#ACACAC', alpha=.6)
    ax0.yaxis.set_major_locator(mticker.MaxNLocator(nbins=4, prune='upper'))
    
    
    plt.subplots_adjust(left=.065, bottom=.08, right=.96, top=.96, wspace=.15, hspace=0.1)
    plt.close() # 关窗口
    canvas =FigureCanvasTkAgg(fig, master=v)  # 设置tkinter绘图区
    canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=1)
    return ax


def axview2t(v,df,t,n=2):
    #显示K线,带6条均线
    data=df.copy()
    data.sort_values(by='date',ascending=True,inplace=True)
    df2=df.copy()
    df2.sort_values(by='date',ascending=True,inplace=True)
    del df2['date']   
    df2['date']=df2.index
    days =df2.reindex(columns=['date','open','high','low','close'])  
    data=data[['date','open','close','high','low','volume']]

    # 生成横轴的刻度名字
    date_tickers=data.date.values
    
    weekday_quotes=[tuple([i]+list(quote[1:])) for i,quote in enumerate(data.values)]
   

    ma5=pd.Series.rolling(data.close, 5).mean()   #股票收盘价5日平均线 
    ma10=pd.Series.rolling(data.close, 10).mean() #股票收盘价10日平均线 
    fig = plt.figure(facecolor=g.ubg,figsize=(1,1))
    ax = plt.subplot2grid((7,4), (0,0), rowspan=5, colspan=4, fc=g.ubg)


    def format_date(x,pos=None):
        if x<0 or x>len(date_tickers)-1:
            return ''
        return date_tickers[int(x)]

    ax.xaxis.set_major_locator(mticker.MaxNLocator(8))  #x轴分成几等分 
    ax.xaxis.set_major_formatter(ticker.FuncFormatter(format_date))    
    candlestick_ohlc(ax, days.values, width=.6, colorup='#ff1717', colordown='#53c156')  
    ax.grid(True, color='r')
    
    ax.xaxis.label.set_color(g.ufg)
    ax.yaxis.label.set_color(g.ufg)
    plt.legend() # 显示图中右上角的提示信息。
    
    ax1=plt.subplot2grid((7,4), (5,0),sharex=ax,rowspan=2, colspan=4, fc=g.ubg)
    ax2=ax_VOL1t(ax1,data) 
    ax.yaxis.label.set_color(g.ufg)
    plt.gca().yaxis.set_major_locator(mticker.MaxNLocator(prune='upper'))

    
    plt.suptitle(t,color=g.ufg)
    plt.subplots_adjust(left=.075, bottom=.08, right=.96, top=.96, wspace=.15, hspace=0.1)
    plt.close() # 关窗口
    canvas =FigureCanvasTkAgg(fig, master=v)  # 设置tkinter绘图区
    canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=1)
    return ax


def axview2(v,df,t,n=2):
    #显示K线,带6条均线
    df2=df.copy()
    # 生成横轴的刻度名字
    date_tickers=df2.date.values
    del df2['date']   
    df2['date']=df2.index
    ma5=pd.Series.rolling(df2.close, 5).mean()   #股票收盘价5日平均线 
    ma10=pd.Series.rolling(df2.close, 10).mean() #股票收盘价10日平均线 
    fig = plt.figure(facecolor=g.ubg,figsize=(1,1))
    ax = plt.subplot2grid((7,4), (0,0), rowspan=5, colspan=4, fc=g.ubg)
    days = df2.reindex(columns=['date','open','high','low','close'])   
    def format_date(x,pos=None):
        if x<0 or x>len(date_tickers)-1:
            return ''
        return date_tickers[int(x)]

    ax.xaxis.set_major_locator(mticker.MaxNLocator(8))  #x轴分成几等分 
    ax.xaxis.set_major_formatter(ticker.FuncFormatter(format_date))  

    ax.tick_params(axis='y', colors=g.ufg)
    ax.tick_params(axis='x', colors=g.ufg)
    plt.ylabel('Stock price')
    candlestick_ohlc(ax, days.values, width=.6, colorup='#ff1717', colordown='#53c156')      
    ax.plot(days.date.values,ma5,label='MA5', linewidth=1.5)
    ax.plot(days.date.values,ma10,label='MA10', linewidth=1.5)
    if n>=3:
        ma20=pd.Series.rolling(df2.close, 20).mean() #股票收盘价20日平均线 
        ax.plot(days.date.values,ma20,label='MA20', linewidth=1.5)
    if n>=4:
        ma30=pd.Series.rolling(df2.close, 30).mean() #股票收盘价30日平均线 
        ax.plot(days.date.values,ma30,label='MA30', linewidth=1.5)
    if n>=5:
        ma60=pd.Series.rolling(df2.close, 60).mean() #股票收盘价60日平均线 
        ax.plot(days.date.values,ma60,label='MA60', linewidth=1.5)
    if n>=6:
        ma120=pd.Series.rolling(df2.close, 120).mean() #股票收盘价120日平均线 
        ax.plot(days.date.values,ma120,label='MA120', linewidth=1.5)    
    ax.grid(True, color='r')
    ax.xaxis.set_major_locator(mticker.MaxNLocator(8))  #x轴分成几等分 
    ax.xaxis.label.set_color(g.ufg)
    ax.yaxis.label.set_color(g.ufg)
    plt.legend() # 显示图中右上角的提示信息。
    ax1=plt.subplot2grid((7,4), (5,0),sharex=ax,rowspan=2, colspan=4, fc=g.ubg)
    ax2=ax_VOL(ax1,df2) 
    
    plt.suptitle(t,color=g.ufg)
    plt.subplots_adjust(left=.075, bottom=.08, right=.96, top=.96, wspace=.15, hspace=0.1)
    plt.close() # 关窗口
    canvas =FigureCanvasTkAgg(fig, master=v)  # 设置tkinter绘图区
    canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=1)
    return ax


def axview2b(v,df,t,n=2):
    #叠加成交密度的K线
    df2=df.copy()
    #df2.dropna(inplace=True)  #删除无效数据
    dfmax=df2.close.max()
    dfmin=df2.close.min()
    l=len(df2)
    if l<80:
        l=int(l/2)
    else:
        l=40
        
    a=(dfmax-dfmin)/l
    x=dfmin
    mm=[]
    while x<=dfmax:
        mm.append(x)
        x+=a

    mma=pd.Series( mm,name='m')
    df4=mma.to_frame('p')
    df4['v']=0
    for i in df2.index:
        j=int((df2.close.loc[i]-dfmin)/a)
        if j>=l:
            j-=1
        df4.v.loc[j]=df4.v.loc[j]+df2.close.loc[i]
        
    date_tickers=df2.date.values
    del df2['date']   
    df2['date']=df2.index
    ma5=pd.Series.rolling(df2.close, 5).mean()   #股票收盘价5日平均线 
    ma10=pd.Series.rolling(df2.close, 10).mean() #股票收盘价10日平均线 
    fig = plt.figure(facecolor=g.ubg,figsize=(1,1))
    ax = plt.subplot2grid((7,4), (0,0), rowspan=5, colspan=4, fc=g.ubg)
    days = df2.reindex(columns=['date','open','high','low','close'])   
    def format_date(x,pos=None):
        if x<0 or x>len(date_tickers)-1:
            return ''
        return date_tickers[int(x)]

    ax.xaxis.set_major_locator(mticker.MaxNLocator(8))  #x轴分成几等分 
    ax.xaxis.set_major_formatter(ticker.FuncFormatter(format_date))  
    ax.tick_params(axis='y', colors=g.ufg)
    ax.tick_params(axis='x', colors=g.ufg)
    plt.ylabel('Stock price')
    candlestick_ohlc(ax, days.values, width=.6, colorup='#ff1717', colordown='#53c156')      
    ax.plot(days.date.values,ma5,label='MA5', linewidth=1.5)
    ax.plot(days.date.values,ma10,label='MA10', linewidth=1.5)
    if n>=3:
        ma20=pd.Series.rolling(df2.close, 20).mean() #股票收盘价20日平均线 
        ax.plot(days.date.values,ma20,label='MA20', linewidth=1.5)
    if n>=4:
        ma30=pd.Series.rolling(df2.close, 30).mean() #股票收盘价30日平均线 
        ax.plot(days.date.values,ma30,label='MA30', linewidth=1.5)
    if n>=5:
        ma60=pd.Series.rolling(df2.close, 60).mean() #股票收盘价60日平均线 
        ax.plot(days.date.values,ma60,label='MA60', linewidth=1.5)
    if n>=6:
        ma120=pd.Series.rolling(df2.close, 120).mean() #股票收盘价120日平均线 
        ax.plot(days.date.values,ma120,label='MA120', linewidth=1.5)    
    ax.grid(True, color='r')
    ax.xaxis.set_major_locator(mticker.MaxNLocator(8))  #x轴分成几等分 
    ax.xaxis.label.set_color(g.ufg)
    ax.yaxis.label.set_color(g.ufg)
    plt.legend() # 显示图中右上角的提示信息。
    
    ax0 = ax.twiny()
    ax0.barh(df4.p,df4.v, height=0.05, align='center', color='#ACACAC', alpha=.6)
    ax0.yaxis.set_major_locator(mticker.MaxNLocator(nbins=8, prune='upper'))
    
    ax1=plt.subplot2grid((7,4), (5,0),sharex=ax,rowspan=2, colspan=4, fc=g.ubg)
    ax2=ax_VOL(ax1,df2) 
    
    plt.suptitle(t,color=g.ufg)
    plt.subplots_adjust(left=.075, bottom=.08, right=.96, top=.96, wspace=.15, hspace=0.1)
    plt.close() # 关窗口
    canvas =FigureCanvasTkAgg(fig, master=v)  # 设置tkinter绘图区
    canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=1)
    return ax

#其中参数v是tkinter的子窗口id，df是股票数据库。
#t是ax画面标题，f是指标名称，例如VOL，KDJ，MACD等等。
def axview2x(v,df,t,n=2,f='VOL'):
    #叠加成交密度的K线
    df2=df.copy()
    #df2.dropna(inplace=True)  #删除无效数据
    dfmax=df2.close.max()
    dfmin=df2.close.min()
    l=len(df2)
    if l<80:
        l=int(l/2)
    else:
        l=40
        
    a=(dfmax-dfmin)/l
    x=dfmin
    mm=[]
    while x<=dfmax:
        mm.append(x)
        x+=a

    mma=pd.Series( mm,name='m')
    df4=mma.to_frame('p')
    df4['v']=0
    for i in df2.index:
        j=int((df2.close.loc[i]-dfmin)/a)
        if j>=l:
            j-=1
        df4.v.loc[j]=df4.v.loc[j]+df2.close.loc[i]
        
    date_tickers=df2.date.values
    del df2['date']   
    df2['date']=df2.index
    ma5=pd.Series.rolling(df2.close, 5).mean()   #股票收盘价5日平均线 
    ma10=pd.Series.rolling(df2.close, 10).mean() #股票收盘价10日平均线 
    fig = plt.figure(facecolor=g.ubg,figsize=(1,1))
    ax = plt.subplot2grid((7,4), (0,0), rowspan=5, colspan=4, fc=g.ubg)
    days = df2.reindex(columns=['date','open','high','low','close'])   
    def format_date(x,pos=None):
        if x<0 or x>len(date_tickers)-1:
            return ''
        return date_tickers[int(x)]

    ax.xaxis.set_major_locator(mticker.MaxNLocator(8))  #x轴分成几等分 
    ax.xaxis.set_major_formatter(ticker.FuncFormatter(format_date))  
    ax.tick_params(axis='y', colors=g.ufg)
    ax.tick_params(axis='x', colors=g.ufg)
    plt.ylabel('Stock price')
    candlestick_ohlc(ax, days.values, width=.6, colorup='#ff1717', colordown='#53c156')      
    ax.plot(days.date.values,ma5,label='MA5', linewidth=1.5)
    ax.plot(days.date.values,ma10,label='MA10', linewidth=1.5)
    if n>=3:
        ma20=pd.Series.rolling(df2.close, 20).mean() #股票收盘价20日平均线 
        ax.plot(days.date.values,ma20,label='MA20', linewidth=1.5)
    if n>=4:
        ma30=pd.Series.rolling(df2.close, 30).mean() #股票收盘价30日平均线 
        ax.plot(days.date.values,ma30,label='MA30', linewidth=1.5)
    if n>=5:
        ma60=pd.Series.rolling(df2.close, 60).mean() #股票收盘价60日平均线 
        ax.plot(days.date.values,ma60,label='MA60', linewidth=1.5)
    if n>=6:
        ma120=pd.Series.rolling(df2.close, 120).mean() #股票收盘价120日平均线 
        ax.plot(days.date.values,ma120,label='MA120', linewidth=1.5)    
    ax.grid(True, color='r')
    ax.xaxis.set_major_locator(mticker.MaxNLocator(8))  #x轴分成几等分 
    ax.xaxis.label.set_color(g.ufg)
    ax.yaxis.label.set_color(g.ufg)
    plt.legend() # 显示图中右上角的提示信息。
    
    ax0 = ax.twiny()
    ax0.barh(df4.p,df4.v, height=0.05, align='center', color='#ACACAC', alpha=.6)
   
    ax1=plt.subplot2grid((7,4), (5,0),sharex=ax,rowspan=2, colspan=4, fc=g.ubg)
    ss='ax2=ax_'+f.strip()+'(ax1,df2)'
    try:
        exec(ss)
    except Exception as e:
        print('用户代码'+ss+'出错:', str(e))

    plt.suptitle(t,color=g.ufg)
    plt.subplots_adjust(left=.075, bottom=.08, right=.96, top=.96, wspace=.15, hspace=0.1)
    plt.close() # 关窗口
    canvas =FigureCanvasTkAgg(fig, master=v)  # 设置tkinter绘图区
    canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=1)
    return ax


def axview3x(v,df,t,n=2,f1='VOL',f2='MACD'):
    #叠加成交密度的K线
    df2=df.copy()
        
    date_tickers=df2.date.values
    del df2['date']   
    df2['date']=df2.index
    ma5=pd.Series.rolling(df2.close, 5).mean()   #股票收盘价5日平均线 
    ma10=pd.Series.rolling(df2.close, 10).mean() #股票收盘价10日平均线 
    fig = plt.figure(facecolor=g.ubg,figsize=(1,1))
    ax = plt.subplot2grid((7,4), (0,0), rowspan=4, colspan=4, fc=g.ubg)
    days = df2.reindex(columns=['date','open','high','low','close'])   
    def format_date(x,pos=None):
        if x<0 or x>len(date_tickers)-1:
            return ''
        return date_tickers[int(x)]

    ax.xaxis.set_major_locator(mticker.MaxNLocator(8))  #x轴分成几等分 
    ax.xaxis.set_major_formatter(ticker.FuncFormatter(format_date))  
    ax.tick_params(axis='y', colors=g.ufg)
    ax.tick_params(axis='x', colors=g.ufg)
    plt.ylabel('Stock price')
    candlestick_ohlc(ax, days.values, width=.6, colorup='#ff1717', colordown='#53c156')      
    ax.plot(days.date.values,ma5,label='MA5', linewidth=1.5)
    ax.plot(days.date.values,ma10,label='MA10', linewidth=1.5)
    if n>=3:
        ma20=pd.Series.rolling(df2.close, 20).mean() #股票收盘价20日平均线 
        ax.plot(days.date.values,ma20,label='MA20', linewidth=1.5)
    if n>=4:
        ma30=pd.Series.rolling(df2.close, 30).mean() #股票收盘价30日平均线 
        ax.plot(days.date.values,ma30,label='MA30', linewidth=1.5)
    if n>=5:
        ma60=pd.Series.rolling(df2.close, 60).mean() #股票收盘价60日平均线 
        ax.plot(days.date.values,ma60,label='MA60', linewidth=1.5)
    if n>=6:
        ma120=pd.Series.rolling(df2.close, 120).mean() #股票收盘价120日平均线 
        ax.plot(days.date.values,ma120,label='MA120', linewidth=1.5)    
    ax.grid(True, color='r')
    #ax.xaxis.set_major_locator(mticker.MaxNLocator(8))  #x轴分成几等分 
    ax.xaxis.label.set_color(g.ufg)
    ax.yaxis.label.set_color(g.ufg)
    plt.legend() # 显示图中右上角的提示信息。
    
   
    ax1=plt.subplot2grid((7,4), (4,0),sharex=ax,rowspan=1, colspan=4, fc=g.ubg)
    ss='axx1=ax_'+f1.strip()+'(ax1,df2)'
    try:
        exec(ss)
    except Exception as e:
        print('用户代码'+ss+'出错:', str(e))

    ax2 =plt.subplot2grid((7,4), (5,0),sharex=ax,rowspan=2, colspan=4, fc=g.ubg)
    ss='axx2=ax_'+f2.strip()+'(ax2,df2)'
    try:
        exec(ss)
    except Exception as e:
        print('用户代码'+ss+'出错:', str(e))

    plt.suptitle(t,color=g.ufg)
    plt.subplots_adjust(left=.075, bottom=.08, right=.96, top=.96, wspace=.15, hspace=0.1)
    plt.close() # 关窗口
    canvas =FigureCanvasTkAgg(fig, master=v)  # 设置tkinter绘图区
    canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=1)
    return ax


def axview4x(v,df,t,n=2,f1='VOL',f2='MACD',f3='KDJ'):
    #叠加成交密度的K线
    df2=df.copy()
 
    date_tickers=df2.date.values
    del df2['date']   
    df2['date']=df2.index
    ma5=pd.Series.rolling(df2.close, 5).mean()   #股票收盘价5日平均线 
    ma10=pd.Series.rolling(df2.close, 10).mean() #股票收盘价10日平均线 
    fig = plt.figure(facecolor=g.ubg,figsize=(1,1))
    ax = plt.subplot2grid((9,4), (0,0), rowspan=4, colspan=4, fc=g.ubg)
    days = df2.reindex(columns=['date','open','high','low','close'])   
    def format_date(x,pos=None):
        if x<0 or x>len(date_tickers)-1:
            return ''
        return date_tickers[int(x)]

    ax.xaxis.set_major_locator(mticker.MaxNLocator(8))  #x轴分成几等分 
    ax.xaxis.set_major_formatter(ticker.FuncFormatter(format_date))  
    ax.tick_params(axis='y', colors=g.ufg)
    ax.tick_params(axis='x', colors=g.ufg)
    plt.ylabel('Stock price')
    candlestick_ohlc(ax, days.values, width=.6, colorup='#ff1717', colordown='#53c156')      
    ax.plot(days.date.values,ma5,label='MA5', linewidth=1.5)
    ax.plot(days.date.values,ma10,label='MA10', linewidth=1.5)
    if n>=3:
        ma20=pd.Series.rolling(df2.close, 20).mean() #股票收盘价20日平均线 
        ax.plot(days.date.values,ma20,label='MA20', linewidth=1.5)
    if n>=4:
        ma30=pd.Series.rolling(df2.close, 30).mean() #股票收盘价30日平均线 
        ax.plot(days.date.values,ma30,label='MA30', linewidth=1.5)
    if n>=5:
        ma60=pd.Series.rolling(df2.close, 60).mean() #股票收盘价60日平均线 
        ax.plot(days.date.values,ma60,label='MA60', linewidth=1.5)
    if n>=6:
        ma120=pd.Series.rolling(df2.close, 120).mean() #股票收盘价120日平均线 
        ax.plot(days.date.values,ma120,label='MA120', linewidth=1.5)    
    ax.grid(True, color='r')
    ax.xaxis.set_major_locator(mticker.MaxNLocator(8))  #x轴分成几等分 
    ax.xaxis.label.set_color(g.ufg)
    ax.yaxis.label.set_color(g.ufg)
    plt.legend() # 显示图中右上角的提示信息。
    
 
    ax1=plt.subplot2grid((9,4), (4,0),sharex=ax,rowspan=1, colspan=4, fc=g.ubg)
    ss='axx1=ax_'+f1.strip()+'(ax1,df2)'
    try:
        exec(ss)
    except Exception as e:
        print('用户代码'+ss+'出错:', str(e))

    ax2 =plt.subplot2grid((9,4), (5,0),sharex=ax,rowspan=2, colspan=4, fc=g.ubg)
    ss='axx2=ax_'+f2.strip()+'(ax2,df2)'
    try:
        exec(ss)
    except Exception as e:
        print('用户代码'+ss+'出错:', str(e))

    ax3 =plt.subplot2grid((9,4), (7,0),sharex=ax,rowspan=2, colspan=4, fc=g.ubg)
    ss='axx3=ax_'+f3.strip()+'(ax3,df2)'
    try:
        exec(ss)
    except Exception as e:
        print('用户代码'+ss+'出错:', str(e))

    plt.suptitle(t,color=g.ufg)
    plt.subplots_adjust(left=.075, bottom=.08, right=.96, top=.96, wspace=.15, hspace=0.1)
    plt.close() # 关窗口
    canvas =FigureCanvasTkAgg(fig, master=v)  # 设置tkinter绘图区
    canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=1)
    return ax


def axview5x(v,df,t,n=2,f1='VOL',f2='MACD',f3='KDJ',f4='RSI'):
    #叠加成交密度的K线
    df2=df.copy()
     
    date_tickers=df2.date.values
    del df2['date']   
    df2['date']=df2.index
    ma5=pd.Series.rolling(df2.close, 5).mean()   #股票收盘价5日平均线 
    ma10=pd.Series.rolling(df2.close, 10).mean() #股票收盘价10日平均线 
    fig = plt.figure(facecolor=g.ubg,figsize=(1,1))
    ax = plt.subplot2grid((10,4), (0,0), rowspan=3, colspan=4, fc=g.ubg)
    days = df2.reindex(columns=['date','open','high','low','close'])   
    def format_date(x,pos=None):
        if x<0 or x>len(date_tickers)-1:
            return ''
        return date_tickers[int(x)]

    ax.xaxis.set_major_locator(mticker.MaxNLocator(8))  #x轴分成几等分 
    ax.xaxis.set_major_formatter(ticker.FuncFormatter(format_date))  
    ax.tick_params(axis='y', colors=g.ufg)
    ax.tick_params(axis='x', colors=g.ufg)
    plt.ylabel('Stock price')
    candlestick_ohlc(ax, days.values, width=.6, colorup='#ff1717', colordown='#53c156')      
    ax.plot(days.date.values,ma5,label='MA5', linewidth=1.5)
    ax.plot(days.date.values,ma10,label='MA10', linewidth=1.5)
    if n>=3:
        ma20=pd.Series.rolling(df2.close, 20).mean() #股票收盘价20日平均线 
        ax.plot(days.date.values,ma20,label='MA20', linewidth=1.5)
    if n>=4:
        ma30=pd.Series.rolling(df2.close, 30).mean() #股票收盘价30日平均线 
        ax.plot(days.date.values,ma30,label='MA30', linewidth=1.5)
    if n>=5:
        ma60=pd.Series.rolling(df2.close, 60).mean() #股票收盘价60日平均线 
        ax.plot(days.date.values,ma60,label='MA60', linewidth=1.5)
    if n>=6:
        ma120=pd.Series.rolling(df2.close, 120).mean() #股票收盘价120日平均线 
        ax.plot(days.date.values,ma120,label='MA120', linewidth=1.5)    
    ax.grid(True, color='r')
    ax.xaxis.label.set_color(g.ufg)
    ax.yaxis.label.set_color(g.ufg)
    plt.legend() # 显示图中右上角的提示信息。

    ax1=plt.subplot2grid((10,4), (3,0),sharex=ax,rowspan=1, colspan=4, fc=g.ubg)
    ss='axx1=ax_'+f1.strip()+'(ax1,df2)'
    try:
        exec(ss)
    except Exception as e:
        print('用户代码'+ss+'出错:', str(e))

    ax2 =plt.subplot2grid((10,4), (4,0),sharex=ax,rowspan=2, colspan=4, fc=g.ubg)
    ss='axx2=ax_'+f2.strip()+'(ax2,df2)'
    try:
        exec(ss)
    except Exception as e:
        print('用户代码'+ss+'出错:', str(e))

    ax3 =plt.subplot2grid((10,4), (6,0),sharex=ax,rowspan=2, colspan=4, fc=g.ubg)
    ss='axx3=ax_'+f3.strip()+'(ax3,df2)'
    try:
        exec(ss)
    except Exception as e:
        print('用户代码'+ss+'出错:', str(e))

    ax4 =plt.subplot2grid((10,4), (8,0),sharex=ax,rowspan=2, colspan=4, fc=g.ubg)
    ss='axx4=ax_'+f4.strip()+'(ax4,df2)'
    try:
        exec(ss)
    except Exception as e:
        print('用户代码'+ss+'出错:', str(e))
    plt.suptitle(t,color=g.ufg)
    plt.subplots_adjust(left=.075, bottom=.08, right=.96, top=.96, wspace=.15, hspace=0.1)
    plt.close() # 关窗口
    canvas =FigureCanvasTkAgg(fig, master=v)  # 设置tkinter绘图区
    canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=1)
    return ax


class plotFrame1(Frame): # 继承Frame类  
    def __init__(self, master,df,stn):  

        self.df1=df
        self.stockn=stn
        self.canvas=None
        self.root = master #定义内部变量root 
        
        Frame.__init__(self, master)  
        self.root = master #定义内部变量root  
        self.createPage()  
   
    def createPage(self):  
        df2=self.df1.copy()
        df2.dropna(inplace=True)
        df2.insert(0,'date',df2.index)
        df2=df2.reset_index(level=None, drop=True ,col_level=0, col_fill='')  
        days=df2.copy()
        g.df=df2
        MA1 = g.MA1
        MA2 = g.MA2
        Av1=mylib.G_MA(days['close'],MA1)
        Av2=mylib.G_MA(days['close'],MA2) 
        SP = len(days.date.values[MA2-1:])
        matplotlib.use('TkAgg')
        fig = plt.figure(facecolor=g.ubg)
        ax1 = plt.subplot2grid((7,4), (0,0), rowspan=4, colspan=4, fc=g.ubg)
   
        days = df2.reindex(columns=['date','open','high','low','close','volume'])   
        daysreshape = days.reset_index()
        daysreshape['date']=mdates.date2num(daysreshape['date'].astype(dt.date))
        daysreshape = daysreshape.reindex(columns=['date','open','high','low','close'])   
        candlestick_ohlc(ax1, daysreshape.values, width=.6, colorup='#ff1717', colordown='#53c156')  
                         
        Label1 = str(MA1)+' MA'
        Label2 = str(MA2)+' MA'
        ax1.plot(days.date.values,Av1,'#e1edf9',label=Label1, linewidth=1.5)
        ax1.plot(days.date.values[-SP:],Av2[-SP:],'#4ee6fd',label=Label2, linewidth=1.5)
        ax1.grid(True, color='r')
        ax1.xaxis.set_major_locator(mticker.MaxNLocator(8))
        ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
        ax1.yaxis.label.set_color(g.utg)

        ax1.tick_params(axis='y', colors=g.ufg)
        plt.gca().yaxis.set_major_locator(mticker.MaxNLocator(prune='upper'))
        ax1.tick_params(axis='x', colors=g.ufg)
        plt.ylabel('Stock price')
        plt.legend() # 显示图中右上角的提示信息。

        plt.suptitle(self.stockn,color=g.ufg)
        
        plt.subplots_adjust(left=.04, bottom=.08, right=.96, top=.96, wspace=.15, hspace=0.1)
        plt.legend() # 显示图中右上角的提示信息。
        self.canvas =FigureCanvasTkAgg(fig, master=self.root)
        self.canvas.draw()
        self.canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        plt.close() # 关窗口


class UplotFrame(Frame): # 继承Frame类  
    def __init__(self, master):  
        self.canvas=None
        self.root = master #定义内部变量root 
        Frame.__init__(self, master)  
        self.createPage()  
   
    def createPage(self):  
        matplotlib.use('TkAgg')
        fig = plt.figure(facecolor=g.ubg,figsize=(7,4))
        self.canvas =FigureCanvasTkAgg(fig, master=self.root)
        self.canvas.draw()
        self.canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        plt.close() # 关窗口
        
        
class plotFrame(Frame): # 继承Frame类  
    def __init__(self, master,df,stn,index):  

        self.df1=df
        self.stockn=stn
        self.index=index
        g.index=index
        self.canvas=None
        self.root = master #定义内部变量root 
        
        Frame.__init__(self, master)  
        self.root = master #定义内部变量root  
        self.createPage()  
   
    def createPage(self):  
        df2=self.df1.copy()
        df2.insert(0,'date',df2.index)
        df2=df2.reset_index(level=None, drop=True ,col_level=0, col_fill='')  
        days=df2.copy()
        g.df=df2
        MA1 = g.MA1
        MA2 = g.MA2
        Av1=mylib.G_MA(days['close'],MA1)
        Av2=mylib.G_MA(days['close'],MA2) 
        SP = len(days.date.values[MA2-1:])
        matplotlib.use('TkAgg')
        fig = plt.figure(facecolor=g.ubg,figsize=(7,4))
        ax1 = plt.subplot2grid((7,4), (0,0), rowspan=4, colspan=4, fc=g.ubg)
        days = df2.reindex(columns=['date','open','high','low','close','volume'])   
        daysreshape = days.reset_index()
        daysreshape['date']=mdates.date2num(daysreshape['date'].astype(dt.date))
        daysreshape = daysreshape.reindex(columns=['date','open','high','low','close'])   
        
        
        candlestick_ohlc(ax1, daysreshape.values, width=.6, colorup='#ff1717', colordown='#53c156')  
                         
        Label1 = str(MA1)+' MA'
        Label2 = str(MA2)+' MA'
        ax1.plot(days.date.values,Av1,'#e1edf9',label=Label1, linewidth=1.5)
        ax1.plot(days.date.values[-SP:],Av2[-SP:],'#4ee6fd',label=Label2, linewidth=1.5)
        ax1.grid(True, color='r')
        ax1.xaxis.set_major_locator(mticker.MaxNLocator(10))
        ax1.yaxis.label.set_color(g.utg)

        ax1.tick_params(axis='y', colors=g.ufg)
        plt.gca().yaxis.set_major_locator(mticker.MaxNLocator(prune='upper'))
        ax1.tick_params(axis='x', colors=g.ufg)
        plt.ylabel('Stock price')
        plt.legend() # 显示图中右上角的提示信息。
        ax1v = ax1.twinx()

        ax1v.tick_params(axis='y', colors=g.ufg)
        ax0 = plt.subplot2grid((7,4), (4,0),sharex=ax1,rowspan=1, colspan=4, fc=g.ubg)
        v1=mylib.G_MA(days['volume'],g.MA1)
        v2=mylib.G_MA(days['volume'],g.MA2)
        rsiCol = '#c1f9f7'
        posCol = '#386d13'
        ax0.plot(days.date.values, v1, rsiCol, linewidth=1,label="$MA5$")
        ax0.plot(days.date.values, v2, posCol, linewidth=1,label="$MA10$")
        ax0.bar(days.date.values,days.volume.values, facecolor='#386d13', alpha=.4)
        ax0.yaxis.label.set_color(g.ufg)

        ax0.tick_params(axis='y', colors=g.ufg)
        ax0.tick_params(axis='x', colors=g.ufg)
        ax0.yaxis.set_major_locator(mticker.MaxNLocator(nbins=4, prune='upper'))
        ax0.tick_params(axis='x', colors=g.ufg)
        plt.ylabel('volume')    
        plt.legend() # 显示图中右上角的提示信息。                 
        if self.index=='KDJ' :
            mydraw.draw_KDJ(ax1,days,9,3,3)
        if self.index=='MACD' :
            mydraw.draw_MACD(ax1,days,12,26,9)
        if self.index=='RSI' :
            mydraw.draw_RSI(ax1,days,6,12,24)
        if self.index=='OBV' :
            mydraw.draw_OBV(ax1,days,6,12)   
        if self.index=='BOLL' :
            mydraw.draw_BOLL(ax1,days,26)       
        if self.index=='自定义' :
            mydraw.draw_UFN(ax1,days)   
        if self.index=='HPYYX' :
            mydraw.draw_HPYYX(ax1,days)   
        plt.suptitle(self.stockn,color=g.ufg)
        plt.setp(ax0.get_xticklabels(), visible=False)
        plt.setp(ax1.get_xticklabels(), visible=False)
        plt.subplots_adjust(left=.04, bottom=.04, right=.96, top=.96, wspace=.15, hspace=0)
        plt.legend() # 显示图中右上角的提示信息。
        self.canvas =FigureCanvasTkAgg(fig, master=self.root)
        self.canvas.draw()
        self.canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        plt.close() # 关窗口

           
class MainFrame(Frame): # 继承Frame类  
    def __init__(self, master=None):  
        Frame.__init__(self, master)  
        self.canvas=None
        self.stock = StringVar()
        self.stock.set('  ')
        self.root = master #定义内部变量root  
        self.createPage() 
        
    def rtnkey(self,event=None):
        aa=self.stock.get()
        aa=mylib.jqsn(aa)
        g.stock=jq.normalize_code(aa)
        self.stock.set(g.stock)
        self.st3()


   
    def createPage(self):  
        # 日期
        Label(self , text='    ').grid(row=0, column=0)
        label1 = Label(self , text='开始日期:  ',ancho=S)
        label1.grid(row=0, column=1)
        # 输入框 (Entry)
        self.date_s = StringVar()
        entrydates = Entry(self, textvariable=self.date_s)
        entrydates.grid(row=0, column=2)
        self.date_s.set(G_sday)
        Label(self , text='    ').grid(row=0, column=3)
        
        label2 = Label(self , text='结束日期:  ')
        label2.grid(row=0, column=4)
        # 输入框 (Entry)
        self.date_e = StringVar()
        entrydatee = Entry(self, textvariable=self.date_e)
        self.date_e.set(G_eday)
        entrydatee.grid(row=0, column=5)
        Label(self , text='    ').grid(row=0, column=6)
        label3 = Label(self , text='股票代码:  ')
        label3.grid(row=0, column=7)
        # 输入框 (Entry)
        
        entrystock = Entry(self, textvariable=self.stock)
        entrystock.grid(row=0, column=8)
        entrystock.bind('<Key-Return>', self.rtnkey)   
        
        
        Label(self , text='    ').grid(row=0, column=9)
        # 按钮  (Button)
        getname = Button(self , text='确认' ,command=self.st)
        getname.grid(row=0, column=10)

        Label(self , text='    ').grid(row=0, column=11)
        label4 = Label(self , text='指标: ')
        label4.grid(row=0, column=12)
        
        # Adding a Combobox
        self.book = tk.StringVar()
        bookChosen = ttk.Combobox(self , width=10, textvariable=self.book)
        bookChosen['values'] = ('KDJ', 'MACD','RSI','OBV','BOLL','自定义')
        bookChosen.grid(row=0, column=13)
        bookChosen.current(0)  #设置初始显示值，值为元组['values']的下标
        bookChosen.config(state='readonly')  #设为只读模式

    def st(self):  
        ds=self.date_s.get()
        de=self.date_e.get()
        stockn=self.stock.get()
        G_index=self.book.get()
        stockn=mylib.jqsn(stockn)
        self.canvas._tkcanvas.pack_forget()
        G_stock=stockn
        matplotlib.use('TkAgg')
        df1 = jq.get_price(stockn,start_date=ds,end_date=de, frequency='daily') # 获取000001.XSHE的2015年的按天数据
        df2=df1.copy()
        df2.insert(0,'date',df2.index)
        df2=df2.reset_index(level=None, drop=True ,col_level=0, col_fill='')  
        days=df2
        G_df=df2
        MA1 = G_MA1
        MA2 = G_MA2
        Av1=mylib.MA(days['close'],MA1)
        Av2=mylib.MA(days['close'],MA2) 
        SP = len(days.date.values[MA2-1:])
        SP1 = len(days.date.values[MA1-1:])
        fig = plt.figure(facecolor='#07000d',figsize=(7,4))
        ax1 = plt.subplot2grid((7,4), (0,0), rowspan=4, colspan=4, fc=g.ubg)
        daysreshape = days.reset_index()
        daysreshape['date']=mdates.date2num(daysreshape['date'].astype(dt.date))
        daysreshape = daysreshape.reindex(columns=['date','open','high','low','close'])   
        candlestick_ohlc(ax1, daysreshape.values, width=.6, colorup='#ff1717', colordown='#53c156')                
        Label1 = str(MA1)+' MA'
        Label2 = str(MA2)+' MA'
        ax1.plot(days.date.values,Av1,'#e1edf9',label=Label1, linewidth=1.5)
        ax1.plot(days.date.values[-SP:],Av2[-SP:],'#4ee6fd',label=Label2, linewidth=1.5)
        ax1.grid(True, color='r')
        ax1.xaxis.set_major_locator(mticker.MaxNLocator(10))
        ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
        ax1.xaxis.label.set_color(g.utg)
        ax1.yaxis.label.set_color(g.utg)
        ax1.spines['bottom'].set_color("#5998ff")
        ax1.spines['top'].set_color("#5998ff")
        ax1.spines['left'].set_color("#5998ff")
        ax1.spines['right'].set_color("#5998ff")
        ax1.tick_params(axis='y', colors=g.utg)
        plt.gca().yaxis.set_major_locator(mticker.MaxNLocator(prune='upper'))
        ax1.tick_params(axis='x', colors=g.utg)
        plt.ylabel('Stock price')
        ax1v = ax1.twinx()
        ax1v.spines['bottom'].set_color("#5998ff")
        ax1v.spines['top'].set_color("#5998ff")
        ax1v.spines['left'].set_color("#5998ff")
        ax1v.spines['right'].set_color("#5998ff")
        ax1v.tick_params(axis='x', colors=g.utg)
        ax1v.tick_params(axis='y', colors=g.utg)
        ax0 = plt.subplot2grid((7,4), (4,0),sharex=ax1,rowspan=1, colspan=4, fc=g.ubg)
        v1=mylib.MA(days['volume'],G_MA1)
        v2=mylib.MA(days['volume'],G_MA2)
        rsiCol = '#c1f9f7'
        posCol = '#386d13'
        negCol = '#8f2020'
        ax0.plot(days.date.values, v1, rsiCol, linewidth=1)
        ax0.plot(days.date.values, v2, posCol, linewidth=1)
        ax0.bar(days.date.values,days.volume.values, facecolor='yellow', alpha=.4)
        ax0.yaxis.label.set_color(g.utg)
        ax0.spines['bottom'].set_color("#5998ff")
        ax0.spines['top'].set_color("#5998ff")
        ax0.spines['left'].set_color("#5998ff")
        ax0.spines['right'].set_color("#5998ff")
        ax0.tick_params(axis='y', colors=g.utg)
        ax0.tick_params(axis='x', colors=g.utg)
        ax0.yaxis.set_major_locator(mticker.MaxNLocator(nbins=4, prune='upper'))#plt.gca().yaxis.set_major_locator(mticker.MaxNLocator(nbins=4,prune='upper'))
        ax0.tick_params(axis='x', colors=g.utg)
        plt.ylabel('volume')                     
        if G_index=='KDJ' :
            mydraw.draw_KDJ(ax1,days,9,3,3)
        if G_index=='MACD' :
            mydraw.draw_MACD(ax1,days,12,26,9)
        if G_index=='RSI' :
            mydraw.draw_RSI(ax1,days,6,12,24)
        if G_index=='OBV' :
            mydraw.draw_OBV(ax1,days,6,12)    
        if G_index=='BOLL' :
            mydraw.draw_BOLL(ax1,days,26)   
        if G_index=='自定义' :
            mydraw.draw_UFN(ax1)   
        plt.suptitle(stockn,color=g.utg)
        plt.setp(ax0.get_xticklabels(), visible=False)
        plt.setp(ax1.get_xticklabels(), visible=False)
        plt.subplots_adjust(left=.04, bottom=.04, right=.96, top=.96, wspace=.15, hspace=0)
        self.canvas =FigureCanvasTkAgg(fig, master=self.root)
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        plt.close() # 关窗口
        

#由于tkinter中没有ToolTip功能，所以自定义这个功能如下
class ToolTip(object):
    def __init__(self, widget):
        self.widget = widget
        self.tipwindow = None
        self.id = None
        self.x = self.y = 0
 
    def showtip(self, text):
        "Display text in tooltip window"
        self.text = text
        if self.tipwindow or not self.text:
            return
        x, y, _cx, cy = self.widget.bbox("insert")
        x = x + self.widget.winfo_rootx() + 27
        y = y + cy + self.widget.winfo_rooty() +27
        self.tipwindow = tw = tk.Toplevel(self.widget)
        tw.wm_overrideredirect(1)
        tw.wm_geometry("+%d+%d" % (x, y))
 
        label = tk.Label(tw, text=self.text, justify=tk.LEFT,
                      background="#ffffe0", relief=tk.SOLID, borderwidth=1,
                      font=("tahoma", "8", "normal"))
        label.pack(ipadx=1)
 
    def hidetip(self):
        tw = self.tipwindow
        self.tipwindow = None
        if tw:
            tw.destroy()
             

#===================================================================          
def createToolTip( widget, text):
    toolTip = ToolTip(widget)
    def enter(event):
        toolTip.showtip(text)
    def leave(event):
        toolTip.hidetip()
    widget.bind('<Enter>', enter)
    widget.bind('<Leave>', leave)


def deltreeitem(tree):
    x=tree.get_children()
    for item in x:
        tree.delete(item)

def deltree(tree):
    g.scrollBarA.pack_forget() 
    g.scrollBarB.pack_forget() 
    tree.pack_forget()
    g.ttree=None
    g.scrollBarA =None
    g.scrollBarB =None

def creattree(w,df):
    grid_df=df
    grid_ss=grid_df.columns
    grid_colimns=[]
    for s in grid_ss:
        grid_colimns.append(s)
    
    #滚动条
    scrollBarA =tk.Scrollbar(w)
    g.scrollBarA=scrollBarA
    g.scrollBarA.pack(side=tk.RIGHT, fill=tk.Y)

    #Treeview组件，6列，显示表头，带垂直滚动条
    tree = ttk.Treeview(w,columns=(grid_colimns),
                      show="headings",
                      yscrollcommand=g.scrollBarA.set)
    
    for s in grid_colimns:
        #设置每列宽度和对齐方式
        tree.column(s,width=len(s)*30,  anchor='center')
        #设置每列表头标题文本
        tree.heading(s, text=s)
        
    g.scrollBarA.config(command=tree.yview)

    scrollBarB  = tk.Scrollbar(w,orient = HORIZONTAL)
    g.scrollBarB=scrollBarB
    g.scrollBarB.set(0.5,0.2)
    g.scrollBarB.pack(side=tk.TOP, fill=tk.X)
    g.scrollBarB.config(command=tree.xview)
    
    #定义并绑定Treeview组件的鼠标单击事件
    #插入演示数据
    for i in range(len(grid_df)):
        v=[]
        for s in grid_ss:
            #v.append(grid_df.get_value(i, s))
            v.append(grid_df.at[i,s])
        tree.insert('', i, values=v)

    tree.pack(fill=tk.BOTH,expand=tk.YES)


    def pop2():
        g.tabControl.select(g.ta3)
        de=time.strftime('%Y-%m-%d',time.localtime(time.time()))
        df1=hp.get_k_data(g.G_stock,ktype='D',start='2018-01-01',end=de,index=False,autype='qfq')
        df2=hp.tstojq(df1)
        if g.plotPage !=None:
            g.plotPage.canvas._tkcanvas.pack_forget() 
            g.plotPage.pack_forget() 
            g.plotPage=None

        g.plotPage = plotFrame(g.tab2,df2,g.stock,g.formula)  
        g.plotPage.pack(fill=X)

    
    # 创建菜单
    menubar=Menu(w)
    # 创建第四个菜单项，并 绑定事件
    menubar.add_command(label='历史行情',command=pop2)


    
    def onDBClick(event):
        item = tree.selection()[0]
        aa=tree.item(item, "values")
        #print("you clicked on  "+item, tree.item(item, "values"))
        bb=list(aa)
        #print(bb[0])
        g.G_stock=bb[0]


    tree.bind("<Button-1>", onDBClick)
    tree.bind("<Double-1>", onDBClick)



    return tree 

def mygrid(w,df):
    grid_df=df
    grid_ss=grid_df.columns
    grid_colimns=[]
    for s in grid_ss:
        grid_colimns.append(s)
    
    #滚动条
    scrollBarA =tk.Scrollbar(w)
    g.scrollBarA=scrollBarA
    g.scrollBarA.pack(side=tk.RIGHT, fill=tk.Y)

    #Treeview组件，6列，显示表头，带垂直滚动条
    tree = ttk.Treeview(w,columns=(grid_colimns),
                      show="headings",
                      yscrollcommand=g.scrollBarA.set)
    
    for s in grid_colimns:
        #设置每列宽度和对齐方式
        #tree.column(s, anchor='center')
        tree.column(s,width=len(s)*30,  anchor='center')
        #设置每列表头标题文本
        tree.heading(s, text=s)
        
    g.scrollBarA.config(command=tree.yview)

    scrollBarB  = tk.Scrollbar(w,orient = HORIZONTAL)
    g.scrollBarB=scrollBarB
    g.scrollBarB.set(0.5,0.2)
    g.scrollBarB.pack(side=tk.TOP, fill=tk.X)
    g.scrollBarB.config(command=tree.xview)
    
    #定义并绑定Treeview组件的鼠标单击事件

    #插入演示数据
    for i in range(len(grid_df)):
        v=[]
        for s in grid_ss:
            v.append(grid_df.at[i,s])
        tree.insert('', i, values=v)


    tree.pack(fill=tk.BOTH,expand=tk.YES)
    
    def onDBClick(event):
        item = tree.selection()[0]
        aa=tree.item(item, "values")
        bb=list(aa)
        g.G_stock=bb[0]

        
        
        
    tree.bind("<Double-1>", onDBClick)
    
    def pop1():
        g.tabControl.select(g.tab2)
        de=time.strftime('%Y-%m-%d',time.localtime(time.time()))
        df1=hp.get_k_data(g.G_stock,ktype='D',start='2018-01-01',end=de,index=False,autype='qfq')
        df2=hp.tstojq(df1)
        if g.plotPage !=None:
            g.plotPage.canvas._tkcanvas.pack_forget() 
            g.plotPage.pack_forget() 
            g.plotPage=None

        g.plotPage = plotFrame(g.tab2,df2,g.G_stock,g.G_index)  
        g.plotPage.pack(fill=X)

        

    def topwin():
        author_ui = Toplevel()
        author_ui.title('子窗口测试')
        author_ui.geometry('200x80')
        about_string = Label(author_ui, text = '这是一个测试！')
        confirmButton = Button(author_ui, text = '确定',
                               command = lambda: self.destroy_ui(author_ui))
        about_string.pack()
        confirmButton.pack()
    
    # 创建菜单
    menubar=Menu(w)
    # 创建第四个菜单项，并 绑定事件
    menubar.add_command(label='历史行情',command=pop1)
    
    def pop(event):
        # Menu 类里面有一个 post 方法，它接收两个参数，即 x 和y 坐标，它会在相应的位置弹出菜单。
        menubar.post(event.x_root,event.y_root)
    
    # 鼠标右键是用的<Button-3>
    # 使用 Menu 类的 pop 方法来弹出菜单
    tree.bind("<Button-3>",pop)    
    return tree
    
    

def myplot(master,df1,stockn='',zb='KDJ'):
    myroot=master
    matplotlib.use('TkAgg')
    plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
    plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
    g.G_index=zb
    
    df2=df1.copy()
    df2.dropna(inplace=True)
    df2.insert(0,'date',df2.index)
    df2=df2.reset_index(level=None, drop=True ,col_level=0, col_fill='')  
    days=df2
    G_df=df2
    MA1 = g.MA1
    MA2 = g.MA2
    Av1=mylib.G_MA(days['close'],MA1)
    Av2=mylib.G_MA(days['close'],MA2) 
    SP = len(days.date.values[MA2-1:])
    SP1 = len(days.date.values[MA1-1:])
    fig = plt.figure(facecolor=g.ubg,figsize=(7,4))
    plt.close()

    plt.clf()
    fig = plt.figure(facecolor=g.ubg,figsize=(7,4))

    ax1 = plt.subplot2grid((7,4), (0,0), rowspan=4, colspan=4, fc=g.ubg)
    daysreshape = days.reset_index()
    daysreshape['date']=mdates.date2num(daysreshape['date'].astype(dt.date))
    daysreshape = daysreshape.reindex(columns=['date','open','high','low','close'])   
    candlestick_ohlc(ax1, daysreshape.values, width=.6, colorup='#ff1717', colordown='#53c156')                
    Label1 = str(MA1)+' MA'
    Label2 = str(MA2)+' MA'
    ax1.plot(days.date.values,Av1,'#e1edf9',label=Label1, linewidth=1.5)
    ax1.plot(days.date.values[-SP:],Av2[-SP:],'#4ee6fd',label=Label2, linewidth=1.5)
    ax1.grid(True, color='r')
    ax1.xaxis.set_major_locator(mticker.MaxNLocator(10))
    ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    ax1.yaxis.label.set_color(g.ufg)
    ax1.spines['bottom'].set_color("#5998ff")
    ax1.spines['top'].set_color("#5998ff")
    ax1.spines['left'].set_color("#5998ff")
    ax1.spines['right'].set_color("#5998ff")
    ax1.tick_params(axis='y', colors=g.ufg)
    plt.gca().yaxis.set_major_locator(mticker.MaxNLocator(prune='upper'))
    ax1.tick_params(axis='x', colors=g.ufg)
    plt.ylabel('Stock price')
    ax1v = ax1.twinx()
    ax1v.spines['bottom'].set_color("#5998ff")
    ax1v.spines['top'].set_color("#5998ff")
    ax1v.spines['left'].set_color("#5998ff")
    ax1v.spines['right'].set_color("#5998ff")
    ax1v.tick_params(axis='x', colors=g.ufg)
    ax1v.tick_params(axis='y', colors=g.ufg)
    ax0 = plt.subplot2grid((7,4), (4,0),sharex=ax1,rowspan=1, colspan=4, fc=g.ubg)
    v1=mylib.G_MA(days['volume'],g.MA1)
    v2=mylib.G_MA(days['volume'],g.MA2)
    v3=mylib.G_MA(days['volume'],g.MA3)
    rsiCol = '#c1f9f7'
    posCol = '#386d13'
    negCol = '#8f2020'
    ax0.plot(days.date.values, v1, rsiCol, linewidth=1)
    ax0.plot(days.date.values, v2, posCol, linewidth=1)
    ax0.bar(days.date.values,days.volume.values, facecolor='yellow', alpha=.4)
    ax0.yaxis.label.set_color(g.ufg)
    ax0.spines['bottom'].set_color("#5998ff")
    ax0.spines['top'].set_color("#5998ff")
    ax0.spines['left'].set_color("#5998ff")
    ax0.spines['right'].set_color("#5998ff")
    ax0.tick_params(axis='y', colors=g.ufg)
    ax0.tick_params(axis='x', colors=g.ufg)
    ax0.yaxis.set_major_locator(mticker.MaxNLocator(nbins=4, prune='upper'))#plt.gca().yaxis.set_major_locator(mticker.MaxNLocator(nbins=4,prune='upper'))
    ax0.tick_params(axis='x', colors=g.ufg)
    plt.ylabel('volume')                     
    if g.G_index=='KDJ' :
        ax3=mydraw.draw_KDJ(ax1,days,9,3,3)
    if g.G_index=='MACD' :
        ax3=mydraw.draw_MACD(ax1,days,12,26,9)
    if g.G_index=='RSI' :
        ax3=mydraw.draw_RSI(ax1,days,6,12,24)
    if g.G_index=='OBV' :
        ax3=mydraw.draw_OBV(ax1,days,6,12)   
    if g.G_index=='BOLL' :
        ax3=mydraw.draw_BOLL(ax1,days,26)                  
    plt.suptitle(stockn,color='w')
    plt.setp(ax0.get_xticklabels(), visible=False)
    plt.setp(ax1.get_xticklabels(), visible=False)
    plt.subplots_adjust(left=.04, bottom=.04, right=.96, top=.96, wspace=.15, hspace=0)
    canvas =FigureCanvasTkAgg(fig, master=myroot)
    my=canvas.get_tk_widget()  
    my.pack(fill=tk.BOTH, expand=1)
    plt.close() # 关窗口

    return my


class gridFrame(Frame): # 继承Frame类  
    def __init__(self, master=None):  
        Frame.__init__(self, master)  
        self.root = master #定义内部变量root  
        self.parenta = master
        self.tree=None
        self.dd=1
        self.n=1
        self.timer=None
        self.gn=None
        self.classA=None
        self.stocks=None
        self.root.config(bg='black')
        self.itemName = StringVar()  
        self.createPage()  
   
    
    def createPage(self):  
        self.LBtext=StringVar()
        self.LBtext.set('指数列表')
        self.LB=Label(self, textvariable = self.LBtext,bg="blue",fg="white").pack(fill=X)