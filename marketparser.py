import urllib
import re
class MarketParser():
	def __init__():
		self.stocks=[]
class AlphaVantageParser(MarketParser):
	def __init__(self,apikey):
		self.csv=''
		self.apikey=apikey
	def getCSV(self,function,stock):
		baseurl='https://www.alphavantage.co/'
		params=urllib.urlencode({'function':function,'symbol':stock,'apikey':self.apikey,'datatype':'csv'})
		try:
			f=urllib.urlopen(baseurl+'query?%s'%params)
			self.csv=f.read()
		except:
			print f.info()
			print f.getcode()
		return self.csv
	def getData(self):
		res=dict()
		if self.csv=='':
			return res
		tmp=re.sub(r'\r','',self.csv)
		tmp=tmp.split('\n')
		header=tmp[0].split(',')
		body=tmp[1:]
		for field in header:
			res[field]=[]
		for line in body:
			tmp=line.split(',')
			n=len(tmp)
			for i in range(n):
				res[header[i]].append(tmp[i])
		return res
