from marketparser import *
from apikey import *
class MarketData(dict):
	def __init__(self):
		self.stocks=[]
	def getFromInternet(self):
		stocks=['MSFT','FB','AAPL']
		self.parser=AlphaVantageParser(apikey)
		function='TIME_SERIES_DAILY_ADJUSTED'
		for stock in stocks:
			self[stock]=self.parser.getCSV(function,stock)
		self.stocks=self.keys()
