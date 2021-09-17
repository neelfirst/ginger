#!/usr/bin/env python3

from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import numpy, pandas, io
import mplfinance as mpf
import matplotlib.dates as mpl_dates

def timedeltaYears(entry, now):
  d1 = datetime.fromisoformat(entry)
  d2 = datetime.fromisoformat(now)
  return (d1 - d2) / (365.25 * timedelta(days=1))

def check_date(d:str):
  try:
    obj = datetime.strptime(d, '%Y-%m-%d')
  except ValueError:
    raise ValueError("Incorrect date format, should be YYYY-MM-DD")
    return False
  return True

def getStockPlot(data, name='', volume='no'):
  df = pandas.DataFrame()
  df = pandas.json_normalize(data)
  df['date'] = pandas.to_datetime(df['date'], format="%Y-%m-%d")
  df = df.set_index('date')

  buf = io.BytesIO()
  mpf.plot(df, type='candle', savefig=buf)
  buf.seek(0)
  return buf
