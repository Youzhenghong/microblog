from app import app
#from app import db
import sqlite3
from flask import request
from flask import session	
from flask import render_template, redirect, url_for
from config import DATABASE_URI,basedir



@app.route('/signout', methods = ['GET', 'POST'])
def SignOutNow():
	session['logged_in'] = False
	session.pop('user', None)
	return redirect(url_for('index'))