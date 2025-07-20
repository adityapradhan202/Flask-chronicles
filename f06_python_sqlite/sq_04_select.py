# In this script we will learn about displaying data.
# Before displaying, we will insert some rows.

import sqlite3

# Function for insertion
def insert_data(table_name,
                ID, Name, Address, Salary):
    
    query = f"Insert into {table_name} (ID, NAME, ADDRESS, SALARY) VALUES({ID}, '{Name}', '{Address}', {Salary})"
    conn.execute(query)
    conn.commit()

if __name__ == "__main__":
    # Set a connection
    conn = sqlite3.connect('mydatabase2.db')

    # Insert some data
    insert_data(
        table_name="Company",
        ID=2, Name="Aditya Pradhan",
        Address="A712,BH2", Salary=20.3
    )
    insert_data(
        table_name="Company",
        ID=3, Name="Adi",
        Address="A712,BH2", Salary=22.3
    )

    print("\n->Displaying rows of db:")
    cursor = conn.execute("Select ID, NAME, ADDRESS, SALARY from Company")
    for row in cursor:
        print(f"ID: {row[0]}")
        print(f"Name: {row[1]}")
        print(f"Address: {row[2]}")
        print(f"Salary: {row[3]}")

    print("Operation done successfully!")

    conn.close()

"""
Output will look like this:

->Displaying rows of db:
ID: 1
Name: Adi
Address: Room number a712, bh2
Salary: 89.98
ID: 2
Name: Aditya Pradhan
Address: A712,BH2
Salary: 20.3
ID: 3
Name: Adi
Address: A712,BH2
Salary: 22.3
Operation done successfully!
"""