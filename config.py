import os


basedir = os.path.abspath(os.path.dirname(__file__)) + '/database'
DATABASE_URI = os.path.join(basedir, 'app.db')
admin="admin"
adminPassword="admin"	

CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'