import pandas_datareader.data as web 
import pandas as pd
import requests

proxies = {'http': 'http:your proxy:8080'}
headers = {     "Accept":"application/json",
            'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
            "Accept-Encoding":"none",
            "Accept-Language":"en-US,en;q = 0.8",
            "Connection":"keep-alive",
            "Referer":"https://cssspritegenerator.com",
            "User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11"
            }

with requests.Session() as s:
    s.headers = headers
    s.proxies.update(proxies)

index=['SP500','NASDAQCOM']

target = 'SP500'
tsd = web.DataReader(target, 'fred',start= '2000-07-10',session=s).dropna()#jpy
caldata=pd.DataFrame({'ds':pd.to_datetime(tsd.index),'y':tsd[target]})

print(caldata)