#!/usr/bin/env python3

from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import numpy

BASEPATH = "./images/"

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

def create_plot(data, name='', xlabel='date', ylabel='close'):
  df = dict()
  for k in d[0].keys():
    v = []
    for j in range(0,len(d)):
      v.append(d[j][k])
    df[k] = v

  f = plt.figure()
  plt.plot(df[xlabel].to_numpy(), df[ylabel].to_numpy(), label=name)
  plt.legend()
  path = BASEPATH + name + ".svg"
  plt.savefig(path)
  return(path)
