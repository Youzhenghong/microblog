from app import app
#from app import db
import sqlite3
import time
from flask import request
from flask import session	
from flask import render_template
from config import DATABASE_URI,basedir, admin, adminPassword
from flask import request
from flask import session


def addNewPassage(title, text):
	db = sqlite3.connect(DATABASE_URI)
	cur = db.cursor()
	cur.execute("insert into posts(title, contents, datetime, visNum) values('%s','%s','%s', %d)" % (title, text, time.asctime(), 0))
	cur.close()
	db.commit()
	db.close()


@app.route('/admin/post', methods = ['GET', 'POST'])
def Post():
	return render_template("Post.html")

@app.route('/admin/PostNewPassage', methods = ['GET', 'POST'])
def PostNewPassage():
	title = request.form['title']
	text = request.form['text']
	addNewPassage(title, text)
	return "post sucessfully"