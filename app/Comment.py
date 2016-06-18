import sqlite3
from flask import render_template
from flask import request,redirect,url_for
from app import app
from config import DATABASE_URI,basedir
import time

def addComment(comment, id, user):
	db = sqlite3.connect(DATABASE_URI)
	cur = db.cursor()
	cur.execute("insert into comments (contents, datetime, username, passageID) values('%s', '%s', '%s', %d)" 
		     % (comment, time.asctime(), user, id))
	cur.close()
	db.commit()
	db.close()


@app.route('/comment', methods = ['POST'])
def newComment(id=0, user=""):
	comment = unicode(request.form['comment'])
	id = request.args.get("id", "", type = int)
	user = request.args.get("user", "", type = str)
	addComment(comment, id, user)
	return redirect(url_for('displayPost', id = id))