# Connecting to a databse
import sqlite3
# sqlite3 is built in python

conn = sqlite3.connect('mydatabase.db')
# conn is the connection object
# if 'mydatabase.db' doesn't exist a db of this name will be created

print("Connection established!")
conn.close()
# use the connection object to close the connection
# we must close the connection after our task is performed