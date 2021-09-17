from flask import Flask
from tradier import *
from utils import *

WIDTH = 100 # number of data points to chart

app = Flask(__name__)

def generatePage(name, image):
  string = "<html><head><title>"+name+"</title></head><body><img src="+image+"></body></html>"
  return(string)

@app.route("/")
def hello():
  return('there is no spoon')

@app.route("/<string:name>/")
def say_hello(name):
  start = str((datetime.now() - timedelta(days=WIDTH)).date())
  stop = str(datetime.now().date())
  stock_data = getStockHistory(name, start, stop, interval='daily')
  stock_plot = getStockPlot(stock_data, name, 'date', 'close', volume="no")
  stock_page = generatePage(name, stock_plot)
  return stock_page

if __name__ == "__main__":
  app.run()
