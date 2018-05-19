from marketparser import *
from stock import *
import os.path
class MarketData(dict):
	def __init__(self):
		self.stocks=[]
	def saveCSV(self,stocks):
		for stock in stocks:
			filename=stock+'-'+self.parser.name+'.csv'
			if os.path.isfile(filename):
				print 'file exists.  not saving.'
				return False
			else:
				fp=open(filename,'w')
				fp.write(self[stock]['csv'])
				fp.close()
	def openCSV(self,files):
		for f in files:
			filename=f
			if not os.path.isfile(filename):
				print 'file: '+filename+' does not exist.'
				return False
			fp=open(filename,'r')
			fn=filename.strip('\n')
			fn=fn.strip('\r')
			stock,parser=fn.split('-')
			self[stock]=Stock()
			self[stock]['csv']=fp.read()
	def getFromInternet(self,stocks,parser='AlphaVantage',apikey='demo'):
		if parser=='AlphaVantage':
			self.parser=AlphaVantageParser(apikey)
		elif parser=='Quandl':
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
