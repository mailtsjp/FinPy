import yfinance as yf
import datetime
import pandas as pd

stocks = ["aapl", "xop", "msft" ]
start = datetime.datetime(2018,1,1)
end = datetime.datetime(2019,7,17)
data = yf.download(stocks, start=start, end=end)
data.stack().reset_index().rename(index=str, columns={"level_1": "Symbol"}).sort_values(['Symbol','Date'])
#df = pd.DataFrame(data)
df.to_csv('bank' + '.csv')
