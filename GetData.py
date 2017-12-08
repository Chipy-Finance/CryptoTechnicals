import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import requests
import quandl

os.getcwd()
os.chdir('/Volumes/Data/Chipy/Py-Finance/Crypto/TechnicalAnalysis/')

btc_usd = quandl.get("BITSTAMP/USD")
gdax = quandl.get("GDAX/USD")


btc_usd.head()
btc_usd.tail()
gdax.tail()
btc_usd = btc_usd[['Bid','High','Low','Last','Volume','Last']]
btc_usd.columns = ['Open','High','Low','Close','Volume','Adj Close']
btc_usd.reset_index().to_csv('btc_usd.csv',index=False)
