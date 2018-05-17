import urllib
class MarketParser():
	def __init__():
		self.stocks=[]
class AlphaVantageParser(MarketParser):
	def __init__(self,apikey):
		self.csv=''
		self.apikey=apikey
	def get(self,function,stock):
		baseurl='https://www.alphavantage.co/'
		params=urllib.urlencode({'function':function,'symbol':stock,'apikey':self.apikey,'datatype':'csv'})
		try:
			f=urllib.urlopen(baseurl+'query?%s'%params)
			self.csv=f.read()
		except:
			print f.info()
			print f.getcode()
		return self.csv
