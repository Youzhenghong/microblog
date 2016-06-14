from app import app
from flask import render_template
from Post import getPost
@app.route('/')
@app.route('/index')

def index():
	data = getPost()
	return render_template("index.html", posts = data)