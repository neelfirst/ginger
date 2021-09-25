import os, io
from flask import Flask, request, url_for, render_template, send_file
from tradier import *
from utils import *

INTERVALS = {'daily': 200, 'weekly': 400}

app = Flask(__name__)

def generatePage(name, images):
  string = "<html><head><title>"+name+"</title></head><body>"
  for i in range(0,len(images)):
    p = os.path.join(os.getcwd(), 'static',  name + str(i) + '.png')
    with open(p,'wb') as ifile:
      ifile.write(images[i].read())
    img = url_for('static', filename=name+str(i)+'.png')
    string += "<img src=\""+img+"\"><br>"
  string += "</body></html>"
  return(string)

@app.route("/")
def hello():
  string = "<form method=\"POST\"><input name=\"text\"><input type=\"submit\"></form>"
  return(string)

@app.route("/<string:name>/")
def say_hello(name):
  stock_plots = []
  for i in INTERVALS:
    start = str((datetime.now() - timedelta(days=INTERVALS[i])).date())
    stop = str(datetime.now().date())
    stock_data = getStockHistory(name, start, stop, interval=i)
    stock_plots.append(getStockPlot(stock_data, name, volume="yes"))
  stock_page = generatePage(name, stock_plots)
  return stock_page

if __name__ == "__main__":
  app.run()
