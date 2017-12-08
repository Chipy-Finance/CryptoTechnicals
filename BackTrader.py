import os
from datetime import datetime
import backtrader as bt

os.chdir('/Volumes/Data/Chipy/Py-Finance/Crypto/TechnicalAnalysis/')

class SmaCross(bt.SignalStrategy):
        params = (('pfast', 10), ('pslow', 30),)
        def __init__(self):
            sma1, sma2 = bt.ind.SMA(period=self.p.pfast), bt.ind.SMA(period=self.p.pslow)
            self.signal_add(bt.SIGNAL_LONG, bt.ind.CrossOver(sma1, sma2))

cerebro = bt.Cerebro()

#data = bt.feeds.YahooFinanceData(dataname='YHOO', fromdate=datetime(2011, 1, 1),todate=datetime(2012, 12, 31))
data = bt.feeds.GenericCSVData(dataname='btc_usd.csv',dtformat='%Y-%m-%d',openinterest=-1)


cerebro.adddata(data)

cerebro.addstrategy(SmaCross)
print('Starting Portfolio Value: %.2f' % cerebro.broker.getvalue())
cerebro.run()
print('Final Portfolio Value: %.2f' % cerebro.broker.getvalue())
cerebro.plot()
