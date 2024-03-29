from flask import Flask
from app import app
from user.models import User

@app.route('/user/signup', methods=['POST'])
def signup():
  return User().signup()

@app.route('/user/signout')
def signout():
  return User().signout()

@app.route('/user/login', methods=['POST'])
def login():
  return User().login()

@app.route('/user/insert', methods=['POST'])
def insert():
  return User().insert()

@app.route('/user/reloadspendingtable', methods=['POST'])
def reloadspendingtable():
  return User().reloadspendingtable()