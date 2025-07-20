# Creating a table in database
import sqlite3

conn = sqlite3.connect("mydatabase2.db")
print("DB successfully created!")

# conn.execute() method is used to execut the queries
# Query for creating a table:
# "Create table {Table Name} (VARIABLE1 TYPE, VARIABLE2 TYPE...)"
conn.execute("Create table Company (ID INT, NAME TEXT, ADDRESS TEXT, SALARY FLOAT)")
print("Table created successfully!")

conn.close()