from matplotlib import pyplot as plt
import mplfinance as mpf
from matplotlib.pylab import date2num
import pandas as pd
import datetime



def make_kline(csvname):
   # quotes = []

   daily = pd.read_csv(csvname, index_col=0, parse_dates=True)
   # 设置索引，日期类型的索引。
   daily.index = pd.DatetimeIndex(daily.index)

   daily.shape
   daily.head(3)
   daily.tail(3)
   mpf.plot(daily,type='candle',mav=(3,6,9),volume=True)
