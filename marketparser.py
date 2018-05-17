class MarketParser():
	def __init__():
		self.stocks=[]
class AlphaVantageParser(MarketParser):
	def __init__(self,apikey):
		self.csv=''
		self.apikey=apikey
	def get(self,function,stocks):
		import urllib
		baseurl='https://www.alphavantage.co/'
		params=urllib.urlencode({'function':function,'symbol':'MSFT','apikey':self.apikey,'datatype':'csv'})
		f=urllib.urlopen(baseurl+'query?%s'%params)
		print f.info()
		print f.getcode()
		self.csv=f.read()
