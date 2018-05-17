from marketparser import *
from apikey import *
class Stock(dict):
	def __init__(self):
		self['csv']=''
		self['data']=''
class MarketData(dict):
	def __init__(self):
		self.stocks=[]
	def getFromInternet(self):
		#stocks=['MSFT','FB','AAPL']
		stocks=['MSFT']
		self.parser=AlphaVantageParser(apikey)
		function='TIME_SERIES_DAILY_ADJUSTED'
		for stock in stocks:
			newStock=Stock()
			s=self.parser.getCSV(function,stock)
			newStock['csv']=s
			s=self.parser.getData()
			newStock['data']=s
			self[stock]=newStock
		self.stocks=self.keys()
