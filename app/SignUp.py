import sqlite3
from flask import render_template
from flask import request
from app import app
from config import DATABASE_URI,basedir

def validate_create(username):
	db = sqlite3.connect(DATABASE_URI)
	cur = db.cursor()
	cur.execute("select username from user where username='%s'" % username)
	query = cur.fetchall()
	print query
	if query:
		cur.close()
		db.commit()
		db.close()
		return False
	else:
		return True 
def add_account(username, password):
	db = sqlite3.connect(DATABASE_URI)
	cur = db.cursor()
	cur.execute("insert into user (username,password) values('%s', '%s')" % (username, password))
	cur.close()
	db.commit()
	db.close()



@app.route('/signup/create', methods = ['GET', 'POST'])
def createAccount():
	username = unicode(request.form['username'])
	password = unicode(request.form['password'])
	if validate_create(username):
		add_account(username, password)
		return render_template("SignIn.html")
	else:
		return render_template("SignUp.html", warning = "account exists,pls choose another one")