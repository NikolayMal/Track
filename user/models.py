from flask import Flask, jsonify, request, session, redirect
from passlib.hash import pbkdf2_sha256
from app import db
import uuid
from datetime import datetime

class User:

  def start_session(self, user):
    del user['password']
    session['logged_in'] = True
    session['user'] = user
    return jsonify(user), 200

  def signup(self):
    # print(request.form)

    # Create the user object
    user = {
      "_id": uuid.uuid4().hex,
      "name": request.form.get('name'),
      "email": request.form.get('email'),
      "password": request.form.get('password')
    }

    # Encrypt the password
    user['password'] = pbkdf2_sha256.encrypt(user['password'])

    # Check for existing email address
    if db.users.find_one({ "email": user['email'] }):
      return jsonify({ "error": "Email address already in use" }), 400

    if db.users.insert_one(user):
      return self.start_session(user)

    return jsonify({ "error": "Signup failed" }), 400
  
  def signout(self):
    session.clear()
    return redirect('/')
  
  def login(self):

    user = db.users.find_one({
      "email": request.form.get('email')
    })

    if user and pbkdf2_sha256.verify(request.form.get('password'), user['password']):
      return self.start_session(user)
    
    return jsonify({ "error": "Invalid login credentials" }), 401

  def insert(self):
    # print(request.form)

    if 'user' in session:
      user = session['user']

    item = {
      "_id": uuid.uuid4().hex,
      "user": user['_id'],
      "item": request.form.get('item'),
      "type": request.form.get('type'),
      "price": request.form.get('price'),
      "datetime": str(datetime.utcnow())
    }
    
    if db.items.insert_one(item):
      return jsonify({ "success": "Insert Success" }), 200

    return jsonify({ "error": "Insert Failed" }), 402

  def reloadspendingtable(self):
    dbdata = ()
    datat = ()

    if 'user' in session:
      user = session['user']
    
    if db.items.find_one( { "user" : user['_id']}):
      for dbdoc in db.items.find( { "user" : user['_id']}):
        date_posted = dbdoc['datetime']
        dbdata = (dbdoc['item'], dbdoc['type'], dbdoc['price'], date_posted[:10])
        datat = datat + (dbdata, )
    else:
      return jsonify({ "error" : "Reload Error"}), 403

    # Sort by date
    print(datat)
    datat = sorted(datat, key=lambda t: t[3], reverse=True)
    print(datat)
    return jsonify({ "success": datat }), 201

    