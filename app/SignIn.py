from app import app
from flask import render_template
@app.route('/signin/sign')
def SignInNow():
	return "Sign in sucecessfully!!!"