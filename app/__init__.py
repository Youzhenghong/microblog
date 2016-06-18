from flask import Flask

from database import connectSqliteDB


app = Flask(__name__)
app.config.from_object('config')

from app import views
from app import SignIn
from app import SignUp
from app import SignOut
from app import Nevigate
from app import Post
from app import Edit
from app import Comment