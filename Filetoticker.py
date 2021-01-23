
import pandas_datareader.data as web
import datetime
 
 
#read ticker symbols from a file to python symbol list
symbol = []
with open('tickers.txt') as f:  
    for line in f:
        symbol.append(line.strip())
f.close
 
 
#datetime is a Python module
 
#datetime.datetime is a data type within the datetime module
#which allows access to Gregorian dates and today function
 
#datetime.date is another data type within the datetime module
#which permits arithmetic with Gregorian date components
 
#definition of end with datetime.datetime type must precede
#definition of start with datetime.date type
 
#the start expression collects data that are up to five years old
 
end = datetime.datetime.today()
 
start = datetime.date(end.year-5,1,1)
 
#set path for csv file
path_out = 'c:/python_programs_output/'
 
 
#loop through 50 tickers in symbol list with i values of 0 through 49
 
#if no historical data returned on any pass, try to get the ticker data again
 
#for first ticker symbol write a fresh copy of csv file for historical data
#on remaining ticker symbols append historical data to the file written for
#the first ticker symbol and do not include a header row
 
i=0
while i<len(symbol):
    try:
        df = web.DataReader(symbol[i], 'yahoo', start, end)
        df.insert(0,'Symbol',symbol[i])
        df = df.drop(['Adj Close'], axis=1)
        if i == 0:
            df.to_csv(path_out+'yahoo_prices_volumes_for_ST_50_to_csv_demo.csv')
            print (i, symbol[i],'has data stored to csv file')
        else:
            df.to_csv(path_out+'yahoo_prices_volumes_for_ST_50_to_csv_demo.csv',mode = 'a',header=False)
            print (i, symbol[i],'has data stored to csv file')
    except:
        print("No information for ticker # and symbol:")
        print (i,symbol[i])
        continue
    i=i+1