from marketdata import *
from apikey import *
md1=MarketData()
md2=MarketData()
#stocks=['MSFT','FB','AAPL']
#stocks=['MSFT']
#stocks=['FB']
stocks=['NDX']
#stocks=['SPY','XUS.TO']
md1.getFromInternet(stocks,'AlphaVantage',av_apikey)
md1.display('csv')
md1.display('data')
md1.getCombined()
md1.display('all')
md1.saveCSV(stocks)
md2.getFromInternet(stocks,'Quandl',quandl_apikey)
md2.display('csv')
md2.display('data')
md2.getCombined()
md2.display('all')
md2.saveCSV(stocks)
md3=MarketData()
md3.openCSV(['NDX-alphavantage.csv'])
md3.display('csv')
md3.display('data')
