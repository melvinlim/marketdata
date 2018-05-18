from marketparser import *
from stock import *
class MarketData(dict):
	def __init__(self):
		self.stocks=[]
	def getFromInternet(self,stocks,parser='av',apikey='demo'):
		if parser=='av':
			self.parser=AlphaVantageParser(apikey)
		elif parser=='qd':
			self.parser=QuandlParser(apikey)
		function='TIME_SERIES_DAILY_ADJUSTED'
		for stock in stocks:
			newStock=Stock()
			s=self.parser.getCSV(function,stock)
			newStock['csv']=s
			s=self.parser.getData()
			newStock['data']=s
			self[stock]=newStock
		self.stocks=self.keys()
	def display(self,target):
		if target=='csv':
			for stock in self.keys():
				data=self[stock]['csv']
				print data
		if target=='data':
			for stock in self.keys():
				data=self[stock]['data']
				for line in data:
					print line
		if target=='all':
			data=self['all']
			for date in data.keys():
				for stock in data[date].keys():
					print date,stock,data[date][stock]
	def getCombined(self):
		res=dict()
		for stock in self.keys():
			data=self[stock]['data']
			for line in data:
				ts=line['timestamp']
				if ts not in res:
					res[ts]=dict()
				res[ts][stock]=line
		self['all']=res
		return res
