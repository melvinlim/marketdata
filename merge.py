target='SPY'
fp=open(target+'-alphavantage.csv')
newData=fp.read()
newData=newData.split('\r\n')
header=newData[0]
newData=newData[1:]
print newData[0][:10]
