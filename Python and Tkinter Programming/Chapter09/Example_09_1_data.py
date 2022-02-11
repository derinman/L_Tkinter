
#  Tag   Run  RFlag  Units   Key 
PRIMARY_DATA = [
  ('DI', 1, 'OL',  'mV',   'di'),
  ('DI', 0, '',    'mV',   'di'),
  ('OH', 1, 'OL.', 'Ohm',  'oh200o'),
  ('OH', 0, '4',   'Ohm',  'oh200o'),
  ('OH', 1, '.OL', 'KOhm', 'oh2ko'),
  ('OH', 0, '2',   'KOhm', 'oh2ko'),
  ('OH', 1, 'O.L', 'KOhm', 'oh20ko'),
  ('OH', 0, '3',   'KOhm', 'oh20ko'),
  ('OH', 1, 'OL.', 'KOhm', 'oh200ko'),
  ('OH', 0, '4',   'KOhm', 'oh200ko'),
  ('OH', 1, '.OL', 'MOhm', 'oh2mo'),
  ('OH', 0, '2',   'MOhm', 'oh2mo'),
  ('OH', 1, 'O.L', 'MOhm', 'oh20mo'),
  ('OH', 0, '3',   'MOhm', 'oh20mo'),
  ('OH', 1, 'OL',  'MOhm', 'oh2000mo'),
  ('OH', 0, '',    'MOhm', 'oh2000mo'),
  ('CA', 0, '2',   'nF',   'calo'),
  ('CA', 0, '2',   'uF',   'cahi'),
  ('DC', 0, '4',   'mV',   'dc200mv'),
  ('DC', 0, '2',   'V',    'dc2v'),
  ('DC', 0, '3',   'V',    'dc20v'),
  ('DC', 0, '4',   'V',    'dc200v'),
  ('DC', 0, '',    'V',    'dc1000v'),
  ('AC', 0, '4',   'mV',   'ac200mv'),
  ('AC', 0, '2',   'V',    'ac2v'),
  ('AC', 0, '3',   'V',    'ac20v'),
  ('AC', 0, '4',   'V',    'ac200v'),
  ('AC', 0, '',    'V',    'ac1000v'),
  ('DC', 0, '4',   'uA',   'dc200ua'),
  ('DC', 0, '2',   'mA',   'dc2ma'),
  ('DC', 0, '3',   'mA',   'dc20ma'),
  ('DC', 0, '4',   'mA',   'dc200ma'),
  ('DC', 0, '3',   'A',    'dc20a'),
  ('AC', 0, '4',   'uA',   'ac200ua'),
  ('AC', 0, '2',   'mA',   'ac2ma'),
  ('AC', 0, '3',   'mA',   'ac20ma'),
  ('AC', 0, '4',   'mA',   'ac200ma'),
  ('AC', 0, '3',   'A',    'ac20a'),
  ('FR', 0, '2',   'Hz',   'frh'),
  ('FR', 0, '2',   'KHz',  'frk'),
  ('FR', 0, '2',   'MHz',  'frm'),
  ('HF', 0, '',    '',     'hfe'),
  ('LO', 0, '',    '',     'logic'),
  ('XX', 0, '',    '',     'cont')]

SECONDARY_DATA = {
#  Key       m  u  A  m  V  k  M  O  n  u  F  M  K  Hz AC Control, Label
'di':       (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 'diode', 'DIO'),
'oh200o':   (0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, '200Ohm', ''),
'oh2ko':    (0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, '2KOhm', ''),
'oh20ko':   (0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, '20KOhm', ''),
'oh200ko':  (0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, '200KOhm', ''),
'oh2mo':    (0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, '2MOhm', ''),
'oh20mo':   (0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, '20MOhm', ''),
'oh2000mo': (0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, '2000MOhm', ''),
'calo':     (0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 'locap', ''),
'cahi':     (0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 'hicap', ''),
'dc200mv':  (0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '200mV', ''),
'dc2v':     (0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '2V', ''),
'dc20v':    (0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '20V', ''),
'dc200v':   (0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '200V', ''),
'dc1000v':  (0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '1000V', ''),
'ac200mv':  (0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, '200mV', ''),
'ac2v':     (0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, '2V', ''),
'ac20v':    (0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, '20V', ''),
'ac200v':   (0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, '200V', ''),
'ac1000v':  (0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, '1000V', ''),
'dc200ua':  (0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '200uA', ''),
'dc2ma':    (1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '2mA', ''),
'dc20ma':   (1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '20mA', ''),
'dc200ma':  (1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '200mA', ''),
'dc20a':    (0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, '20A', ''),
'ac200ua':  (0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, '200uA', ''),
'ac2ma':    (1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, '2mA', ''),
'ac20ma':   (1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, '20mA', ''),
'ac200ma':  (1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, '200mA', ''),
'ac20a':    (0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, '20A', ''),
'frh':      (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 'freq', 'FREQ'),
'frk':      (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 'freq', 'FREQ'),
'frm':      (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 'freq', 'FREQ'),
'hfe':      (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 'hfe', 'HFE'),
'logic':    (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 'logic', 'LOGI'),
'cont':     (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 'cont', '')}


TESTDATA = ['DI    OL   mV', 'DI    OL   mV', 'DI    OL   mV', 
            'DI    OL   mV', 'DI    OL   mV', 'DI    OL   mV',
            'DI  0422   mV', 'DI  0022   mV', 'DI  0003   mV',
            'DI  0001   mV', 'DI  0004   mV', 'DI  0001   mV',
            'DI  0001   mV', 'DI  0001   mV', 'DI  0892   mV',
            'DI    OL   mV', 'DI    OL   mV', 'DI    OL   mV',
            'DI    OL   mV', 'DI    OL   mV', 'DI    OL   mV',
            'DI  0623   mV', 'DI  0036   mV', 'DI  0034   mV',
            'DI  0154   mV', 'DI  0055   mV', 'DI  0018   mV',
            'DI  0084   mV', 'DI  0020   mV', 'DI  0007   mV',
            'DI    OL   mV', 'OH   OL.  Ohm', 'OH   OL.  Ohm',
            'OH   OL.  Ohm', 'OH   OL.  Ohm', 'OH   OL.  Ohm',
            'OH   OL.  Ohm', 'OH   OL.  Ohm', 'OH  007.8 Ohm',
            'OH  014.7 Ohm', 'OH  001.1 Ohm', 'OH  116.3 Ohm',
            'OH  018.3 Ohm', 'OH  002.9 Ohm', 'OH  003.0 Ohm',
            'OH   OL.  Ohm', 'OH   .OL KOhm', 'OH   .OL KOhm',
            'OH   .OL KOhm', 'OH   .OL KOhm', 'OH -0.010KOhm',
            'OH  0.085KOhm', 'OH  0.001KOhm', 'OH  0.001KOhm',
            'OH  0.047KOhm', 'OH  0.410KOhm', 'OH  0.277KOhm',
            'OH  0.005KOhm', 'OH  0.006KOhm', 'OH   .OL KOhm',
            'OH   O.L KOhm', 'OH   O.L KOhm', 'OH  01.80KOhm',
            'OH  00.05KOhm', 'OH  00.71KOhm', 'OH  00.02KOhm',
            'OH  00.12KOhm', 'OH  00.00KOhm', 'OH  00.00KOhm',
            'OH  00.00KOhm', 'OH  00.72KOhm', 'OH   OL. KOhm',
            'OH   OL. KOhm', 'OH   OL. KOhm', 'OH   OL. KOhm',
            'OH   OL. KOhm', 'OH   OL. KOhm', 'OH -001.5KOhm',
            'OH  000.0KOhm', 'OH  000.0KOhm', 'OH  000.0KOhm',
            'OH  000.0KOhm', 'OH  000.0KOhm', 'OH  000.0KOhm',
            'OH  000.0KOhm', 'OH   OL. KOhm', 'OH   .OL MOhm',
            'OH   .OL MOhm', 'OH   .OL MOhm', 'OH   .OL MOhm',
            'OH   .OL MOhm', 'OH   .OL MOhm', 'OH -0.008MOhm',
            'OH  0.000MOhm', 'OH  0.000MOhm', 'OH  0.000MOhm',
            'OH  0.000MOhm', 'OH  0.000MOhm', 'OH  0.000MOhm',
            'OH  0.000MOhm', 'OH  0.349MOhm', 'OH   O.L MOhm',
            'OH   O.L MOhm', 'OH   O.L MOhm', 'OH -00.15MOhm',
            'OH  00.00MOhm', 'OH  00.00MOhm', 'OH  00.00MOhm',
            'OH  00.00MOhm', 'OH  00.00MOhm', 'OH  00.00MOhm',
            'OH  00.00MOhm', 'OH  00.00MOhm', 'OH  00.00MOhm',
            'OH  00.00MOhm', 'OH  00.58MOhm', 'OH  02.53MOhm',
            'OH  0022 MOhm', 'OH  0016 MOhm', 'OH  0035 MOhm',
            'OH  0048 MOhm', 'OH  0089 MOhm', 'OH  0156 MOhm',
            'OH  0270 MOhm', 'OH  0459 MOhm', 'OH  0594 MOhm',
            'OH  0991 MOhm', 'OH  1564 MOhm', 'OH  0000 MOhm',
            'OH  0000 MOhm', 'OH  0000 MOhm', 'OH  0000 MOhm',
            'OH  0001 MOhm', 'OH  0008 MOhm', 'CA  0.001  nF',
            'CA  0.000  nF', 'CA  0.000  nF', 'CA  0.000  nF',
            'CA  0.000  nF', 'CA  0.000  nF', 'CA  0.000  uF',
            'CA  0.000  uF', 'CA  0.000  uF', 'CA  0.000  uF',
            'DC  034.1  mV', 'DC  025.6  mV', 'DC  063.5  mV',
            'DC  072.3  mV', 'DC  040.7  mV', 'DC  017.5  mV',
            'DC  005.2  mV', 'DC  0.005   V', 'DC  0.002   V',
            'DC  0.001   V', 'DC  0.001   V', 'DC  0.001   V',
            'DC -0.003   V', 'DC  0.003   V', 'DC  0.004   V',
            'DC  0.001   V', 'DC -0.002   V', 'AC  0.010   V',
            'AC  0.014   V', 'AC  0.016   V', 'AC  0.012   V',
            'AC  00.11   V', 'AC  00.00   V', 'AC  00.00   V',
            'AC  00.00   V', 'AC  00.00   V', 'AC  00.00   V',
            'AC  00.00   V', 'AC  00.00   V', 'AC  003.0   V',
            'AC  000.0   V', 'AC  000.0   V', 'AC  000.0   V',
            'AC  000.0   V', 'AC  000.0   V', 'AC  000.0   V',
            'DC  000.0   V', 'DC  0001    V', 'DC  0000    V',
            'DC  0000    V', 'DC  0000    V', 'DC  0000    V',
            'DC  0000    V', 'DC  0000    V', 'DC  0000    V',
            'DC  0000    V', 'DC  0000    V', 'DC  0001    V',
            'DC  000.0  uA', 'DC  000.0  uA', 'DC  000.0  uA',
            'DC  000.0  uA', 'DC  000.0  uA', 'DC  000.0  uA',
            'DC  000.0  uA', 'DC  0.000  mA', 'DC  0.000  mA',
            'DC  0.000  mA', 'DC  0.000  mA', 'DC  0.000  mA',
            'DC  0.000  mA', 'DC  0.000  mA', 'DC  0.000  mA',
            'DC  0.000  mA', 'DC  00.00  mA', 'DC  00.00  mA',
            'DC  00.00  mA', 'DC  00.00  mA', 'DC  00.00  mA',
            'DC  00.00  mA', 'DC  00.00  mA', 'DC  00.00  mA',
            'DC  00.00  mA', 'DC  000.0  mA', 'DC  000.0  mA',
            'DC  000.0  mA', 'DC  000.0  mA', 'DC  000.0  mA',
            'DC  000.0  mA', 'DC  000.0  mA', 'DC  000.0  mA',
            'DC  000.0  mA', 'DC  00.00   A', 'DC  00.00   A',
            'DC  00.00   A', 'DC  00.00   A', 'DC  00.00   A',
            'DC  00.00   A', 'DC  00.00   A', 'FR  0.001 KHz',
            'FR  0.000 KHz', 'FR  0.001 KHz', 'FR  0.001 KHz',
            'FR  0.002 KHz', 'FR  0.000 KHz', 'FR  0.001 KHz',
            'FR  0.001 KHz', 'FR  0.000 KHz', 'HF  0000     ',
            'HF  0000     ', 'HF  0000     ', 'HF  0000     ',
            'HF  0000     ', 'HF  0000     ', 'HF  0000     ',
            'HF  0000     ', 'LO   rdy     ', 'LO   rdy     ',
            'LO   rdy     ', 'LO   rdy     ', 'LO   rdy     ',
            'LO   rdy     ', 'LO - rdy     ' ]

#m  u  A  m  V  k  M  O  n  u  F  M  K  Hz AC Control, Label
PANEL_LABELS = [ (225,  80, 'Arial',  'M', 'mhz'),
                 (240,  80, 'Arial',  'K', 'khz'),
                 (255,  80, 'Arial',  'Hz', 'hz'),
                 (225,  95, 'Arial',  'm', 'ma'),
                 (240,  95, 'Symbol', 'm', 'ua'),
                 (255,  95, 'Arial',  'A', 'a'),
                 (240, 110, 'Arial',  'm', 'mv'),
                 (255, 110, 'Arial',  'V', 'v'),
                 (225, 125, 'Arial',  'K', 'ko'),
                 (240, 125, 'Arial',  'M', 'mo'),
                 (255, 125, 'Symbol', 'W', 'o'),
                 (225, 140, 'Arial',  'n', 'nf'),
                 (240, 140, 'Symbol', 'm', 'uf'),
                 (255, 140, 'Arial',  'F', 'f'),
                 (50,  110, 'Arial',  'AC','ac')]

 
