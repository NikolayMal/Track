from flask import Flask, render_template, session, redirect
from flask_session import Session
from functools import wraps
from pymongo import MongoClient
from mongopass import mongopass

app = Flask(__name__)
app.secret_key = b'\xcc^\x91\xeb\x17-\xd0W\x03\xa7\xf8J0\xac8\xc5'

# Database
client = MongoClient(mongopass)
db = client.curd
myCollection = db.myColl

# Session
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Decorators
def login_required(f):
  @wraps(f)
  def wrap(*args, **kwargs):
    if 'logged_in' in session:
      return f(*args, **kwargs)
    else:
      return redirect('/')
  
  return wrap

def logged_in(f):
  @wraps(f)
  def wrap(*args, **kwargs):
    if 'logged_in' in session:
      return redirect('/dashboard')
    else:
      return f(*args, **kwargs)
  return wrap

# Routes
from user import routes

@app.route('/')
@logged_in
def home():
  return render_template('home.html')

@app.route('/dashboard/')
@login_required
def dashboard():
  return render_template('dashboard.html')

@app.route('/datatable/')
@login_required
def datatable():
  return render_template('datatable.html')

@app.route('/graphs/')
@login_required
def graphs():
  return render_template('graphs.html')


if __name__ == "__main__":
  app.run(port=5000, debug=True)