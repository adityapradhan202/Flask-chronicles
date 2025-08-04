# cursor object is used to execute sql queries
# it is recommended to use cursor, to execute the queries
# conn can also execute the queries
# but multiple cursor can execute queries independtly, within one single connection
# cursors are basically iterables
# We can iterate over cursor to get individual rows, provided that cursor has selected and fetched some rows

import sqlite3

# connection
conn = sqlite3.connect('posts.db')

# row_factory means how the row will behave
# rows of cursor will be treated as dictionaries
conn.row_factory = sqlite3.Row

cur = conn.cursor()
cur.execute("""
    CREATE TABLE IF NOT EXISTS posts (id INTEGER PRIMARY KEY AUTOINCREMENT, content TEXT NOT NULL)
""")

# id will be automatically added (unique value for every new row)
# there is auto increment
# and it is also the primary key

# selecting everything from database
cur.execute("SELECT * FROM posts") # Prepares the result set
rows = cur.fetchall() # Actually retrieves all rows

print(rows) # It will return empty rows because we don't have anything here

# Inserting some values
# Query: Insert into table (col1, col2, col3) VALUES (?, ?, ?), (actual tuple of values that will come in place of placeholders ?)
# ? is a placeholder for the data you want to insert. It’s a way to safely insert data without risking SQL injection attacks.

content_tuple1 = ("Hello my name is Aditya",)
content_tuple2 = ("I love machine learning and AI",)
content_tuple3 = ("I would be really happy if I could become a DSML dev",)
cur.execute("INSERT INTO posts (content) VALUES (?)", content_tuple1)
cur.execute("INSERT INTO posts (content) VALUES (?)", content_tuple2)
cur.execute("INSERT INTO posts (content) VALUES (?)", content_tuple3)

cur.execute("SELECT * FROM posts")
rows = cur.fetchall()
for row in rows:
    print(row["id"])
    print(row["content"])

# Updating some values
pid = 1
content = "New content here!!!!!!"
cur.execute("UPDATE posts SET content=? WHERE id=?", (content, pid))

# Deleting one row
cur.execute("DELETE FROM posts WHERE id=?", (2,))

print()
cur.execute("SELECT * FROM posts")
rows = cur.fetchall()
for row in rows:
    print(row["id"])
    print(row["content"])

# commit the changes
conn.commit()

# close cursor
# release the data cursor is holding
cur.close()

# connection close
conn.close()