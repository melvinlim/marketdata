from marketdata import *
md=MarketData()
#stocks=['MSFT','FB','AAPL']
#stocks=['MSFT']
stocks=['SPY','XUS.TO']
md.getFromInternet(stocks)
md.display('csv')
md.display('data')
md.getCombined()
md.display('all')
