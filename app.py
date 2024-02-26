from flask import Flask, render_template, request
from database import *
app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("home.html")

@app.route("/login", methods = ['post'])
def login():
  data = request.form
  return data
if __name__ == "__main__":
  app.run(host='0.0.0.0', port=8080, debug=True)