import sqlite3

# Creating database
conn = sqlite3.connect("mydb.db")
print("Database has been created!")

conn.execute("Create table StudentMarks (ID INT, NAME TEXT, MARKS FLOAT)")
conn.execute("Insert into StudentMarks(ID, NAME, MARKS) VALUES(1, 'Aditya', 45.56)")
conn.commit()

# Updating a value
conn.execute("Update StudentMarks set MARKS = 50 where ID = 1")

# Display
cursor = conn.execute("Select ID, NAME, MARKS from StudentMarks")
for row in cursor:
    print(f"ID = {row[0]}")
    print(f"Name = {row[1]}")
    print(f"Marks = {row[2]}")
print("Operations done successfully")


# Deleting a row
conn.execute("Delete from StudentMarks where ID = 1")
print("Second display:")
for row in cursor:
    print(f"ID = {row[0]}")
    print(f"Name = {row[1]}")
    print(f"Marks = {row[2]}")

# Close connection
conn.close()

"""
Output will look like this:
Database has been created!
ID = 1
Name = Aditya
Marks = 50.0
Operations done successfully
Second display:
"""