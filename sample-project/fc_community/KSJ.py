import sqlite3

con = sqlite3.connect('db.sqlite3')
cursor = con.cursor()
cursor.execute("select * from sqlite_master")
print(cursor.fetchall())