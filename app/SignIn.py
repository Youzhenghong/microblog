from app import app
from app import db
from flask import request	
from flask import render_template

def valid_account(username, password):
	return False

@app.route('/signin/sign', methods = ['GET', 'POST'])
def SignInNow():
	username = request.form['username']
	password = request.form['password']
	print username, password
	if valid_account(username, password):
		return "Sign in sucecessfully!!!"
	else:
		return render_template("SignIn.html", warning = "invalid account or password")