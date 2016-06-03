from flask import Flask

from database import sqliteDB


app = Flask(__name__)
app.config.from_object('config')
db = sqliteDB()

from app import views
from app import SignIn
from app import Nevigate

