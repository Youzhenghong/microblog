import sqlite3
import os
from config import DATABASE_URI,basedir

def connectSqliteDB():
	print '%s',DATABASE_URI
	if not os.path.exists(basedir):
		s.mkdir(basedir)
	return sqlite3.connect(DATABASE_URI)
		