import sqlite3
conn = sqlite3.connect('database.sqlite')
print("Opened database successfully")

import pandas as pd
conn.execute('''CREATE TABLE IF NOT EXISTS CLASS_10
         (SNO INT PRIMARY KEY NOT NULL,
         Roll_No INT NOT NULL,
         Name TEXT NOT NULL,
         AGE INT DEFAULT (15),
         GENDER TEXT NOT NULL,
         Email_ID TEXT NOT NULL,
         Contact_No REAL NOT NULL);''')

print("Table created successfully")

conn.execute("INSERT INTO CLASS_10 (SNO,Roll_No,NAME,AGE,Gender,Email_ID,Contact_No) \
      VALUES (1, 1, 'Allen', 14, 'Male', 'allen@gmail.com', 8080900 )");

conn.execute("INSERT INTO CLASS_10 (SNO,Roll_No,NAME,AGE,Gender,Email_ID,Contact_No) \
      VALUES (2, 2, 'Aisha', 14, 'Female', 'aish@gmail.com', 9080900 )");

conn.execute("INSERT INTO CLASS_10 (SNO,Roll_No,NAME,AGE,Gender,Email_ID,Contact_No) \
      VALUES (3, 3, 'Jeff', 15, 'Male', 'allen@gmail.com', 9900900 )");

# Save the changes
conn.commit()
print("Records created successfully")
