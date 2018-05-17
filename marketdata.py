from marketparser import *
from apikey import *
class MarketData(dict):
	def __init__(self):
		self.stocks=[]
	def getInternet(self):
		stocks=['MSFT','FB']
		self.parser=AlphaVantageParser(apikey)
		function='TIME_SERIES_DAILY_ADJUSTED'
		for stock in stocks:
			self[stock]=self.parser.get(function,stock)
