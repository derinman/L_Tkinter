# ch6_8.py
from tkinter import * # Import tkinter

# x = StringVar() # 儲存一個 string 型別變數, 預設值為""
# x = IntVar() # 儲存一個整型變數, 預設值為0
# x = DoubleVar() # 儲存一個浮點型變數, 預設值為0.0
# x = BooleanVar() # 儲存一個布林型變數, 返回值為 0 (代表 False) 或 1 (代表 True)

def cal():
    monthrate = float(rateVar.get()) / (12*100)         # 改成百分比以及月利率
    molecules = float(loanVar.get()) * monthrate
    denominator = 1 - (1 / (1 + monthrate) ** (int(yearVar.get()) * 12))
    monthlypay = int(molecules / denominator)           # 每月還款金額
    monthlypayVar.set(monthlypay)
    totalPay = monthlypay * int(yearVar.get()) * 12
    totalpayVar.set(totalPay)

window = Tk() 
window.title("ch6_8") 
        
Label(window, text="貸款年利率").grid(row=1, column=1, sticky=W)
Label(window, text="貸款年數").grid(row=2, column=1, sticky=W)
Label(window, text="貸款金額").grid(row=3, column=1, sticky=W)
Label(window, text="月付款金額").grid(row=4, column=1, sticky=W)
Label(window, text="總付款金額").grid(row=5, column=1, sticky=W)
        
rateVar = StringVar()
Entry(window,textvariable=rateVar,justify=RIGHT).grid(row=1,column=2,padx=3)
yearVar = StringVar()
Entry(window,textvariable=yearVar,justify=RIGHT).grid(row=2,column=2,padx=3)
loanVar = StringVar()
Entry(window,textvariable=loanVar,justify=RIGHT).grid(row=3,column=2,padx=3)
        
monthlypayVar = StringVar()
lblmonthlypay = Label(window,textvariable=monthlypayVar).grid(row=4,
                      column=2,sticky=E,pady=3)
totalpayVar = StringVar()
lbltotalpay = Label(window,textvariable=totalpayVar).grid(row=5, 
                    column=2,sticky=E,padx=3)
btn_Cal = Button(window,text="計算貸款金額",command=cal).grid(
                 row=6,column=2,sticky=E,padx=3,pady=3)
        
window.mainloop() 


