import pandas as pd
import pandas_datareader as  web
import matplotlib.pyplot as pp
import datetime

# Get SPY data for past several years

SPY_Dat = web.DataReader('SPY', 'yahoo', datetime.date(2007,1,1))

# We are going to use a trailing 252 trading day window
window = 252

# Calculate the max drawdown in the past window days for each day in the series.
# Use min_periods=1 if you want to let the first 252 days data have an expanding window
Roll_Max = SPY_Dat['Adj Close'].rolling(window, min_periods=1).max()
Daily_Drawdown = SPY_Dat['Adj Close']/Roll_Max - 1.0

# Next we calculate the minimum (negative) daily drawdown in that window.
# Again, use min_periods=1 if you want to allow the expanding window
Max_Daily_Drawdown = Daily_Drawdown.rolling(window, min_periods=1).min()

# Plot the results
Daily_Drawdown.plot()
Max_Daily_Drawdown.plot()
pp.show()