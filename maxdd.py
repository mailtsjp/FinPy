# import needed libraries
import quandl
import pandas as pd
from pandas_datareader import data

# add quandl API key for unrestricted
quandl.ApiConfig.api_key = 'shAvzzwDvkzzDq93Kzyy'
QUANDL_API_KEY= 'shAvzzwDvkzzDq93Kzyy'

# get the table for daily stock prices and,
# filter the table for selected tickers, columns within a time range
# set paginate to True because Quandl limits tables API to 10,000 rows per call
#data = quandl.get('WIKI', ticker = ['AAPL', 'MSFT', 'WMT'], 
#                        qopts = { 'columns': ['ticker', 'date', 'open','adj_close'] }, 
#                        date = { 'gte': '2020-01-01', 'lte': '2021-1-15' }, 
#                        paginate=True)

# create a new dataframe with 'date' column as index
#new = data.set_index('date')

# use pandas pivot function to sort adj_close by tickers
#clean_data = new.pivot(columns='ticker')

#tickers2get = ['EOD/AAPL','EOD/COP']

# Define ticker list
#tickers_list =['AAPL','IBM','MSFT']

#import pandas
#data = pd.DataFrame(columns=tickers_list)

# Set the start and end date
start_date = '2020-01-01'
end_date = '2021-01-01'

#fetch data
# Feth the data
data = quandl.get('WIKI/PRICES', ticker = ['AAPL', 'MSFT', 'WMT'], 
                        qopts = { 'columns': ['ticker', 'date', 'adj_close'] }, 
                        date = { 'gte': '2015-12-31', 'lte': '2016-12-31' }, 
                        paginate=True)
# Print first 5 rows of the data
data.head()


# Set the start and end date
#start_date = '1990-01-01'
#end_date = '2018-03-01'
# Set the ticker name
#ticker = 'AMZN'

#getData = quandl.get('WIKI/'+ticker, start_date=start_date, end_date=end_date)
# Print the first 5 rows of the dataframe
#data.head(2)

# check the head of the output
#clean_data.head()
#print(clean_data)


# get the table for daily stock prices and,
# filter the table for selected tickers, columns within a time range
# set paginate to True because Quandl limits tables API to 10,000 rows per call

data = quandl.get_table('WIKI/PRICES', ticker = ['AAPL', 'MSFT', 'WMT'], 
                        qopts = { 'columns': ['ticker', 'date', 'adj_close'] }, 
                        date = { 'gte': '2015-12-31', 'lte': '2016-12-31' }, 
                        paginate=True)
data.head()

# create a new dataframe with 'date' column as index
new = data.set_index('date')

# use pandas pivot function to sort adj_close by tickers
clean_data = new.pivot(columns='ticker')

# check the head of the output
clean_data.head()


import quandl
import pandas as pd
import datetime
from datetime import timedelta 
from pandas import ExcelWriter

quandl.ApiConfig.api_key = 'NL6weZFnRNw5q_L5-Nve'
tickers = ['BA','MSFT','ACN']

data = quandl.get_table('WIKI/PRICES', ticker = tickers, 
                        qopts = { 'columns': ['ticker', 'date', 'open', 'close'] }, 
                        date = { 'gte': '2000-01-01', 'lte': '2018-04-16' }, 
                        paginate=True)

data.reset_index()
data.set_index('date')