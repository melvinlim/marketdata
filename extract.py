from marketdata import *
from apikey import *
md=MarketData()
md2=MarketData()
#stocks=['MSFT','FB','AAPL']
#stocks=['MSFT']
#stocks=['FB']
stocks=['NDX']
#stocks=['SPY','XUS.TO']
md.getFromInternet(stocks,'av',av_apikey)
md.display('csv')
md.display('data')
md.getCombined()
md.display('all')
md.saveCSV(stocks,'1')
md2.getFromInternet(stocks,'qd',quandl_apikey)
md2.display('csv')
md2.display('data')
md2.getCombined()
md2.display('all')
md2.saveCSV(stocks,'2')
