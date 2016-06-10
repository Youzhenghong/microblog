from app import app
from flask import render_template,redirect,url_for


@app.route('/About')
def AboutPage():
	return render_template("About.html")

@app.route('/ContactMe')
def ContactPage():
	return render_template("ContactMe.html")


@app.route('/signin')
def SignIn():
	return render_template("SignIn.html")


@app.route('/signup')
def SignUp():
	return render_template("SignUp.html")

@app.route('/signout')
def SignOut():
	return redirect(url_for('SignOutNow'));
