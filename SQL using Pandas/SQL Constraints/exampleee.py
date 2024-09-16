import sqlite3
conn = sqlite3.connect('database.sqlite')


import pandas as pd
tables = pd.read_sql("""SELECT * 
                    FROM CLASS_10;""", conn)
print(tables)