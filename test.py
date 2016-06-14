from config import DATABASE_URI,basedir, admin, adminPassword


def getPost():
	db = sqlite3.connect(DATABASE_URI)
	cur = db.cursor()
	cur.execute("select * from posts")
	query = cur.fetchall()
	print query