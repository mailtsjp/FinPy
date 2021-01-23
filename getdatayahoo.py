
from pandas_datareader import data
import datetime as dt

import matplotlib.pyplot as plt    
import pandas as pd


#from pandas.io.dat import options
#ticker = 'IBM'
#x = Options(ticker)
#calls,puts = x.get_optins_data()


symbols = ['F','MSFT','XRX','XOM','HD','COP']
#symbols = ['MGK']
for i in symbols:
    stkdata = data.DataReader(i,'yahoo','2018-01-01','2020-04-01').round(2)
    stkdata.iloc[:,[2,3]].to_csv(i+'.csv')
    
    #print(stkdata)
    #print(stkdata.iloc[:,[2,3]])  #'Open','close']])
    
    #d = {"Date":stkdata['Date'], "Ticker":stkdata['Ticker'], "Open":stddata['Open']} #, "High": [""], "Low":[""], "Close":[""], "Volume":[""], "Adj Close":[""]}
    #df1 = pd.DataFrame(data=d)
    #print(df1.head())

"""
ticker = 'BND'
begdate = '2014-11-11'
enddate = '2016-11-11'
# year, month, day
datah = data.DataReader(ticker,'yahoo',begdate,enddate)['date','Adj Close'].to_csv('test.csv')

#datah = data.DataReader(ticker,'yahoo',dt.datetime(2018,1,1),dt.datetime(2019,12,31))

datal = data.DataReader(ticker,'yahoo',dt.datetime(2019,12,1),dt.datetime(2020,12,30))
"""

#datah.to_csv(ticker + '.csv', header = True)
#datah.to_csv('bnd.csv', header = True)

"""
#high
gld_h = pd.DataFrame(datah)
filename = gld_h + '.csv'
#gld_h.to_csv(filename,index = False, header=True)

date_h = pd.to_datetime(list(gld_h.index))
adj_close_h = list(gld_h["Adj Close"])

#low
gld_l = pd.DataFrame(datal)
filename = gld_l + '.csv'
#gld_h.to_csv(filename,index = False, header=True)
date_l = pd.to_datetime(list(gld_l.index))
adj_close_l = list(gld_l["Adj Close"])


#plot
plt.figure()
plt.title("SPDR Gold Shares ")
plt.plot(date_h,adj_close_h,'C1', label='C1')
plt.plot(date_l,adj_close_l,'C2', label='C2')
plt.show()
"""