from app import app
#from app import db
import sqlite3
import time
from flask import request
from flask import session	
from flask import render_template,redirect,url_for
from config import DATABASE_URI,basedir, admin, adminPassword
from flask import request
from flask import session
from Post import getPost


@app.route('/admin/edit', methods = ['GET', 'POST'])
def Edit():
	return render_template("edit.html", posts = getPost())


@app.route('/admin/edit/delete', methods = ['GET', 'POST'])
def deletePassage(id=0	):
	data = getPost(id)
	db = sqlite3.connect(DATABASE_URI)
	cur = db.cursor()
	cur.execute("delete from posts where id = %d" % data[0]['id'])
	cur.close()
	db.commit()
	db.close()
	return redirect(url_for('Edit'))
	