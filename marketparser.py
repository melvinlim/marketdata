import urllib
import re
class MarketParser():
	def __init__():
		self.stocks=[]
	def getData(self):
		res=[]
		if self.csv=='':
			return res
		if re.search(r'Information',self.csv):
			print self.csv
			return []
		if re.search(r'incorrect',self.csv):
			print self.csv
			return []
		tmp=re.sub(r'\r','',self.csv)
		tmp=tmp.strip('\n')
		tmp=tmp.split('\n')
		header=self.modifyHeader(tmp[0])
		self.header=header
		header=header.split(',')
		body=tmp[1:]
		self.body=body
		for line in body:
			dLine=dict()
			tmp=line.split(',')
			n=len(tmp)
			for i in range(n):
				dLine[header[i]]=tmp[i]
			res.append(dLine)
		return res
class AlphaVantageParser(MarketParser):
	def __init__(self,apikey):
		self.csv=''
		self.apikey=apikey
	def modifyHeader(self,header):
		return header
	def getCSV(self,function,stock):
		if self.apikey=='demo':
			function='TIME_SERIES_INTRADAY'
			stock='MSFT'
		baseurl='https://www.alphavantage.co/'
		params=urllib.urlencode({'function':function,'symbol':stock,'apikey':self.apikey,'datatype':'csv'})
		try:
			f=urllib.urlopen(baseurl+'query?%s'%params)
			self.csv=f.read()
		except:
			print f.info()
			print f.getcode()
		return self.csv
class QuandlParser(MarketParser):
	def __init__(self,apikey):
		self.csv=''
		self.apikey=apikey
		if self.apikey=='':
			self.apikey=None
	def modifyHeader(self,header):
		header=re.sub(r'Date','timestamp',header)
		header=header.lower()
		header=re.sub(r'trade timestamp','timestamp',header)
		return header
	def getCSV(self,function,stock):
		if self.apikey:
			#database_code='EOD'
			database_code='NASDAQOMX'
		else:
			database_code='WIKI'
		dataset_code=stock
		return_format='csv'
		baseurl='https://www.quandl.com/api/v3/datasets/'+database_code+'/'+dataset_code+'/data.'+return_format
#		params=urllib.urlencode({'function':function,'symbol':stock,'apikey':self.apikey,'datatype':'csv'})
		if self.apikey:
			params=urllib.urlencode({'api_key':self.apikey})
		else:
			params=''
		try:
			f=urllib.urlopen(baseurl+'?%s'%params)
#			f=urllib.urlopen(baseurl)
			self.csv=f.read()
		except:
			print f.info()
			print f.getcode()
		return self.csv
