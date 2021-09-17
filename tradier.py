#!/usr/bin/env python3
'''
This interface file is specifically for
interacting with the Tradier Brokerage API
and returning pandas-friendly dict-arrays
NKS 2021-09-16
'''

import requests
from utils import *

TOKEN = 'O57RHf8iwaecbcObUXdAInQBOxFF'
ENDPT_ROOT = "https://api.tradier.com/v1/"
HEADER = {'Accept': 'application/json', 'Authorization': 'Bearer '+TOKEN}

def getJsonResponse(endpoint, header, param):
  r = requests.get(endpoint, headers=header, params=param).json()
  return(r)

def getSpotPrice(symbol):
  endpoint = ENDPT_ROOT + "markets/quotes"
  params = {'symbols': symbol, 'greeks': 'true'}
  r = getJsonResponse(endpoint, HEADER, params)['quotes']['quote']['last']
  return(r)

def getStockHistory(symbol, start, stop, interval = 'daily'):
  if not (check_date(start) and check_date(stop)):
    raise ValueError("invalid chart date ranges")
    return None
  if interval not in ['daily', 'weekly', 'monthly']:
    raise ValueError("invalid chart interval")
    return None
  if timedeltaYears(start, stop) >= 0:
    raise ValueError("poorly ordered date range")

  endpoint = ENDPT_ROOT + "markets/history"
  params = {'symbol': symbol, 'interval': interval, 'start': start, 'end': stop}
  r = getJsonResponse(endpoint, HEADER, params)
  if (interval == 'daily'):
    return r['history']['day']
  elif (interval == 'weekly'):
    return r['history']['week'] # TODO: UNTESTED
  elif (interval == 'monthly'):
    return r['history']['month'] # TODO: UNTESTED
  else:
    return None

def getOptionExpirations(symbol):
  endpoint = ENDPT_ROOT + "markets/options/expirations"
  params = {'symbol': symbol, 'includeAllRoots': 'true'}
  r = getJsonResponse(endpoint, HEADER, params)['expirations']['date']
  return(r)

def getOptionChains(symbol):
  x = []
  expiries = getOptionExpirations(symbol)
  endpoint = ENDPT_ROOT + "markets/options/chains"
  for expiry in expiries:
    params = {'symbol': symbol, 'expiration': expiry, 'greeks': 'true'}
    r = getJsonResponse(endpoint, HEADER, params)['options']['option']
    x.extend(r)
  return(x)
