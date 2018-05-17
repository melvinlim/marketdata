from marketdata import *
md=MarketData()
#stocks=['MSFT','FB','AAPL']
stocks=['MSFT']
md.getFromInternet(stocks)
md.display('csv')
md.display('data')
