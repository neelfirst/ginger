#!/usr/bin/env python3

from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import numpy

BASEPATH = "/home/neeljymx/ginger/images/"

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

def getStockPlot(data, name='', xlabel='date', ylabel='close', volume='no'):
  df = dict()
  for k in data[0].keys():
    v = []
    for j in range(0,len(data)):
      v.append(data[j][k])
    df[k] = numpy.array(v)

  f = plt.figure()
  plt.plot(df[xlabel], df[ylabel], label=name)
  plt.legend()
#  path = BASEPATH + name + ".png"
  path = "../images/"+name+".png"
  plt.savefig(path)
  return(path)
