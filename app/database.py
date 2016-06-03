import sqlite3
import os
from config import DATABASE_URI,basedir

class sqliteDB():
	def __init__(self):
		print '%s',DATABASE_URI
		if not os.path.exists(basedir):
			os.mkdir(basedir)
		self.cxn = sqlite3.connect(DATABASE_URI)
		self.cur = self.cxn.cursor()