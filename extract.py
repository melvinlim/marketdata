from marketdata import *
md=MarketData()
md2=MarketData()
#stocks=['MSFT','FB','AAPL']
#stocks=['MSFT']
#stocks=['FB']
stocks=['NDX']
#stocks=['SPY','XUS.TO']
md.getFromInternet(stocks)
md.display('csv')
md.display('data')
md.getCombined()
md.display('all')
md2.getFromInternet(stocks,'qd')
md2.display('csv')
md2.display('data')
md2.getCombined()
md2.display('all')
