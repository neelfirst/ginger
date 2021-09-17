import os, io
from flask import Flask, request, url_for, render_template, send_file
from tradier import *
from utils import *

WIDTH = 100 # number of data points to chart

app = Flask(__name__)

def generatePage(name, image):
  p = os.path.join(os.getcwd(), 'static',  name + '.png')
  with open(p,'wb') as ifile:
    ifile.write(image.read())
  img = url_for('static', filename=name+'.png')
  string = "<html><head><title>"+name+"</title></head><body><img src=\""+img+"\"></body></html>"
  return(string)

@app.route("/")
def hello():
  string = "<form method=\"POST\"><input name=\"text\"><input type=\"submit\"></form>"
  return(string)

@app.route("/<string:name>/")
def say_hello(name):
  start = str((datetime.now() - timedelta(days=WIDTH)).date())
  stop = str(datetime.now().date())
  stock_data = getStockHistory(name, start, stop, interval='daily')
  stock_plot = getStockPlot(stock_data, name, volume="no")
  stock_page = generatePage(name, stock_plot)
  return stock_page

if __name__ == "__main__":
  app.run()
