from marketparser import *
from apikey import *
class MarketData(dict):
	def __init__(self):
		self.stocks=[]
	def getInternet(self):
		stocks=[]
		self.parser=AlphaVantageParser(apikey)
		function='TIME_SERIES_DAILY_ADJUSTED'
		self.parser.get(function,stocks)
