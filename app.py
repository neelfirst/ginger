from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
  return 'hello world'

@app.route("/<string:name>/")
def say_hello(name):
  return f"hello {name}"

if __name__ == "__main__":
  app.run()
