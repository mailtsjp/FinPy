
from pandas_datareader import data
#import pandas_datareader.data as web
import datetime # as dt

import matplotlib.pyplot as plt    
import pandas as pd


#from pandas.io.dat import options
#ticker = 'IBM'
#x = Options(ticker)
#calls,puts = x.get_optins_data()

# Prepare tickers array
#symbols = ['F','MSFT','XRX','XOM','HD','COP']
#symbols = ['MGK']

#Read tickers from fiile
#read ticker symbols from a file to python symbol list
symbol = []
with open('tickersthemes.txt') as f:  
    for line in f:
        symbol.append(line.strip())
f.close


#definition of end with datetime.datetime type must precede
#definition of start with datetime.date type
 
#the start expression collects data that are up to five years old
 
end = datetime.datetime.today()
start = datetime.date(end.year-5,1,1)

#get ticker details
i=0

#while i<len(symbol):
for i in symbol:
    print(i)
    
    try:
        df = data.DataReader(i, 'yahoo', start, end).round(2)
        df.iloc[:,[2,3]].to_csv(i+'.csv')
        #df.insert(0,'Symbol',symbol[i])
        #df = df.drop(['Adj Close'], axis=1)
        """
        if i == 0:
            df.to_csv(path_out+'yahoo_prices_volumes_for_ST_50_to_csv_demo.csv')
              df.to_csv(h_out+'yahoo_prices_volumes_for_ST_50_to_csv_demo.csv')
              print (i, symbol[i],'has data stored to csv file')
        else:
            #df.to_csv(path_out+'yahoo_prices_volumes_for_ST_50_to_csv_demo.csv',mode = 'a',header=False)
            print (i, symbol[i],'has data stored to csv file')
        """
    except:
       # print("No information for ticker # and symbol:")
        #print (i,symbol[i])
        continue
    #i=i+1
"""
for i in symbols:
    stkdata = data.DataReader(i,'yahoo','2018-01-01','2020-04-01').round(2)
    stkdata.iloc[:,[2,3]].to_csv(i+'.csv')
"""    
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