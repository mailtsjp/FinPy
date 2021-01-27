import pandas as pd
import numpy as np 
import datetime
import matplotlib.pyplot as plt 
from matplotlib.ticker import FuncFormatter
from pandas_datareader import data as pdr 

startdate='2015-1-1'
enddate='2020-12-31'

refTicker="mgc"

# Stock objects:
stocks = [
    {
        'ticker': "aapl",
        'name': 'MegaCap',
    }
    ]   

#Method to get stock data
def create_plot(stocks):
    data = pd.DataFrame()
    for stock in stocks:
        #create a column for adj close of each stock
        #use datareader liberary to get dat
        
        data[stock['ticker']] = pdr.DataReader(stock['ticker'], 
            data_source='yahoo',start=startdate)['Adj Close']
    
                # Calculate the returns for all the days
        returns = data.apply(lambda x: (x / x[0] * 100))
       
        #Find max and min
        i = np.argmax(np.maximum.accumulate(data[]) - data[]) # end of the period
        j = np.argmax(data[:i]) # start of period

                
        #for stock in stocks:
        ax[1].plot(returns[stock['ticker']], label=stock['name'],color="green")
        ax[1].legend([stock['name']],loc='best', ncol=10)
        ax[1].plot([i, j], [data[i], data[j]], 'o', color='Red', markersize=10)

 

#gridspec_kw={'hspace': 0}
#figure, ax = plt.subplots(2, sharex=True, sharey=True, gridspec_kw={'hspace': 0}) #(nrows=2,ncols=1)
figure, ax = plt.subplots(2) #, sharex=True, sharey=True, gridspec_kw={'hspace': 0}) #(nrows=2,ncols=1)
figure.suptitle("Historical Drawdowns study")
ax[0].grid(True)
ax[1].grid(True)

ax[0].set_title("Historical Drawdowns")

#ax[1].set_title("Price Trend")

# Hide x labels and tick labels for all but bottom plot.
#for axmerge in ax:
#    axmerge.label_outer()

#plot refererence ticker historical Drawdown
#aapl = pdr.get_data_yahoo('AAPL', start = datetime.datetime(2006,10,1), end = datetime.datetime(2020,12,30))
aapl = pdr.get_data_yahoo(refTicker, start=startdate)
daily_close = aapl[['Adj Close']]
daily_pct_c = daily_close.pct_change()

#Calculate max draawdowns 
wealth_index = 1000*(1+daily_pct_c["Adj Close"]).cumprod()
previous_peaks = wealth_index.cummax()
drawdown = ((wealth_index - previous_peaks)/previous_peaks)
#drawdown.plot()
plt.ylabel('Drawdowns')
ax[0].plot(drawdown,"r-")
for stock in stocks:
    ax[0].legend([stock['name']],loc='best', ncol=10)

#Display Y axis in %
ax[0].yaxis.set_major_formatter(FuncFormatter(lambda y, _: '{:.0%}'.format(y)))


#plot price trend, Normalized pct % in lower subplot
create_plot(stocks)

plt.ylabel('Cummumative returns %')
plt.xlabel('Date')

########
# Major ticks every 20, minor ticks every 5
major_ticks = np.arange(-0.4, 0.1, 0.1)
minor_ticks = np.arange(-0.4, 0.1, 0.05)

ax[0].set_yticks(major_ticks)
ax[0].set_yticks(minor_ticks, minor=True)

#######

plt.show()