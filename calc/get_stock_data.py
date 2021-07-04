


target = 'SP500'
tsd = web.DataReader(target, 'fred',start= '2000-07-10',session=s).dropna()#jpy
caldata=pd.DataFrame({'ds':pd.to_datetime(tsd.index),'y':tsd[target]})

print(caldata)