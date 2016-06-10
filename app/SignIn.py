from app import app
#from app import db
import sqlite3
from flask import request
from flask import session	
from flask import render_template
from config import DATABASE_URI,basedir


def valid_account(username, password):
	db = sqlite3.connect(DATABASE_URI)
	cur = db.cursor()
	cur.execute("select password from user where username='%s'" % username)
	query = cur.fetchall()
	if query:
		if password == unicode(query[0][0]):
			cur.close()
			db.commit()
			db.close()
			return True
	else:
		cur.close()
		db.commit()
		db.close()
		return False


@app.route('/signin/sign', methods = ['GET', 'POST'])
def SignInNow():
	username = unicode(request.form['username'])
	password = unicode(request.form['password'])
	print username
	print password
	if valid_account(username, password):
		session['logged_in'] = True
		session['user'] = username
		return render_template("index.html")
	else:
		return render_template("SignIn.html", warning = "invalid account or password")