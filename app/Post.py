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

def getPost(id=0):
	db = sqlite3.connect(DATABASE_URI)
	cur = db.cursor()
	if not id:
		cur.execute("select * from posts")
	else:
		cur.execute("select * from posts where id='%d'" % id)
	query = cur.fetchall()
	data=[]
	for item in query:
		dicitem={}
		dicitem['id']= item[0]
		dicitem['time'] = item[1]
		dicitem['title'] = item[2]
		dicitem['visNum'] = item[3]
		dicitem['content'] = item[4]
		data.append(dicitem)
	return data

@app.route('/index/article/<int:id>', methods = ['GET', 'POST'])
def displayPost(id):
	data = getPost(id)[0]
	return render_template('index.html',display=True, title=data['title'], text=data['content'], comments = True)



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
	return redirect(url_for('index', display=True, title=title, text=text))


