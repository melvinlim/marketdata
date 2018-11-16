from marketparser import *
from stock import *
import os.path
import pickle
import time
class MarketData(dict):
	def __init__(self,filename=''):
		self.stocks=[]
		self.intraday=[]
		if filename!='':
			fp=open(filename,'r')
			self['all']=pickle.load(fp)
	def saveCombined(self):
		if 'all' not in self:
			print 'combined data not present.'
			return False
		directory=time.strftime('%F')
		if not os.path.isdir(directory):
			os.mkdir(directory)
		filename=directory+'/allData.pkl'
		if os.path.isfile(filename):
			print filename+' exists.  not saving.'
			return False
		fp=open(filename,'w')
		pickle.dump(self['all'],fp)
	def _saveCSV(self,target,filename):
		if os.path.isfile(filename):
			print filename+' exists.  not saving.'
			return False
		else:
			fp=open(filename,'w')
			fp.write(target)
			fp.close()
	def saveCSV(self,stocks):
		t=time.strftime('%F')
		directory=time.strftime('%F')
		if not os.path.isdir(directory):
			os.mkdir(directory)
		for stock in stocks:
			filename=directory+'/'+stock+'_'+'DAILY'+'_'+t+'.csv'
			self._saveCSV(self[stock]['csv'],filename)
			filename=directory+'/'+stock+'_'+'DAILY_ADJ'+'_'+t+'.csv'
			self._saveCSV(self[stock]['adj_csv'],filename)
			filename=directory+'/'+stock+'_'+'INTRADAY'+'_'+t+'.csv'
			self._saveCSV(self[stock]['intraday_csv'],filename)
		filename=directory+'/'+'USDCAD'+'_'+'DAILY'+'_'+t+'.csv'
		self._saveCSV(self['USDCAD']['forex_daily_csv'],filename)
		filename=directory+'/'+'USDCAD'+'_'+'INTRADAY'+'_'+t+'.csv'
		self._saveCSV(self['USDCAD']['forex_intraday_csv'],filename)
	def saveFuturesCSV(self):
		t=time.strftime('%F')
		directory=time.strftime('%F')
		if not os.path.isdir(directory):
			os.mkdir(directory)
		if 'ES' in self:
			if 'CHRIS' in self['ES']:
				filename=directory+'/'+'CHRIS_ES1'+'_'+t+'.csv'
				self._saveCSV(self['ES']['CHRIS'],filename)
			if 'CME' in self['ES']:
				filename=directory+'/'+'CME_ESZ2018'+'_'+t+'.csv'
				self._saveCSV(self['ES']['CME'],filename)
	def openCSV(self,files,apikey='demo'):
		for f in files:
			filename=f
			if not os.path.isfile(filename):
				print 'file: '+filename+' does not exist.'
				return False
			fp=open(filename,'r')
			fn=filename.strip('\n')
			fn=fn.strip('\r')
			fn=fn.strip('.csv')
			stock,parser=fn.split('_')
			print parser
			if parser=='alphavantage':
				self.parser=AlphaVantageParser(apikey)
			elif parser=='quandl':
				self.parser=QuandlParser(apikey)
			self[stock]=Stock()
			csv=fp.read()
			self[stock]['csv']=csv
			data=self.parser.getData(csv)
			self[stock]['data']=data
	def getFromInternet(self,stocks,parser='AlphaVantage',apikey='demo'):
		if parser=='AlphaVantage':
			self.parser=AlphaVantageParser(apikey)
		elif parser=='Quandl':
			self.parser=QuandlParser(apikey)
		for stock in stocks:
			newStock=Stock()
			csv=self.parser.getCSV('TIME_SERIES_DAILY',stock)
			newStock['csv']=csv
			csv=self.parser.getCSV('TIME_SERIES_DAILY_ADJUSTED',stock)
			newStock['adj_csv']=csv
			data=self.parser.getData(csv)
			newStock['data']=data
			self[stock]=newStock
#get intraday data
			csv=self.parser.getCSV('TIME_SERIES_INTRADAY',stock)
			self[stock]['intraday_csv']=csv
#
#get forex data
		newStock=Stock()
		self['USDCAD']=newStock
		csv=self.parser.getCSV('FX_DAILY',None)
		self['USDCAD']['forex_daily_csv']=csv
		csv=self.parser.getCSV('FX_INTRADAY',None)
		self['USDCAD']['forex_intraday_csv']=csv
#
		self.stocks=self.keys()
	def getFutures(self,parser='Quandl',apikey='demo'):
		self.parser=QuandlParser(apikey)
#get futures data
		newStock=Stock()
		self['ES']=newStock
		qdlp=QuandlParser(apikey)
#		csv=self.parser.getCSV('CHRIS',None)
#		self['ES']['CHRIS']=csv
		csv=self.parser.getCSV('CME',None)
		self['ES']['CME']=csv
#
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
