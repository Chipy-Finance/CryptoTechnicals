import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline

os.chdir('/Volumes/Data/Chipy/Py-Finance/Crypto/TechnicalAnalysis/')

rf = 1.3
rf_daily = (1+rf/100)**(1.0/365.0)-1
btc_usd = pd.read_csv('btc_usd.csv')
btc_usd.set_index('Date',inplace=True)
btc_usd.head()
btc_usd['daily_return'] = btc_usd['Adj Close'].pct_change().fillna(0)
btc_usd['daily_return_rel'] = btc_usd['daily_return']-rf_daily
btc_usd['log_return'] = np.log(btc_usd['daily_return']+1)
btc_usd['cumulative_return'] = ((btc_usd['daily_return']+1).cumprod())-1
btc_usd['cumulative_return'].plot()


#Annual Returns
btc_usd['Year'] = btc_usd.index.values
btc_usd['Year'] = btc_usd['Year'].apply(lambda x: pd.to_datetime(x,format='%Y-%m-%d').year)
btc_usd.head()
annual_returns = btc_usd.groupby('Year')['log_return'].sum()
annual_returns = annual_returns.reset_index()
annual_returns['Annual_Return'] = annual_returns['log_return'].apply(lambda x: (np.exp(x)-1)*100)
annual_returns

#Full Returns for Dataset
(np.exp(btc_usd['log_return'].sum())-1)*100


#Calculate Max Drawdown
btc_usd.head()

price_stream = btc_usd[btc_usd.Year==2017][['Close']]
price_stream

i = np.argmax(price_stream.values[:i]) # start of period
j = np.argmax(np.maximum.accumulate(price_stream.values) - price_stream.values) # end of the period

print(price_stream.values[i],price_stream.values[j])

max_drawdown_pct = (price_stream.values[j]/price_stream.values[i]-1)*100
max_drawdown_pct

#Full Dataset Drawdown
price_stream = btc_usd[['Close']]

i = np.argmax(np.maximum.accumulate(price_stream.values) - price_stream.values) # end of the period
j = np.argmax(price_stream.values[:i]) # start of period

print(price_stream.values[i],price_stream.values[j])

max_drawdown_pct = (price_stream.values[j]/price_stream.values[i]-1)*100
max_drawdown_pct


# Calculate the Sharpe Ratio
btc_usd.head()
btc_usd['sharpe_30d'] = btc_usd['daily_return'].rolling(window=30).apply(lambda x: (x.mean()*30.0)/(x.std()*np.sqrt(30.0)))
btc_usd['sharpe_365d'] = btc_usd['daily_return'].rolling(window=365).apply(lambda x: (x.mean()*365.0)/(x.std()*np.sqrt(365.0)))

btc_usd['sharpe_30d'].plot()
btc_usd['sharpe_365d'].plot()

btc_usd[btc_usd.Year==2017]['sharpe_365d'].max()
btc_usd['sharpe_365d'].max()
