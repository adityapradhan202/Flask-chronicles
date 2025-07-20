import sqlite3

conn = sqlite3.connect("mydatabase2.db")

# Query for inserting a row:
# "Insert into {Table name} (col_nam1, col_nam2, ...) VALUES(value1, value2, ...)"
conn.execute("Insert into Company (ID, NAME, ADDRESS, SALARY) VALUES(1, 'Adi', 'Room number a712, bh2', 89.98)")

# Make sure to commit the changes
conn.commit()

print("Records created successfully!")

# Also make sure that connection is closed after tasks are finished
conn.close()