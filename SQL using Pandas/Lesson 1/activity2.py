import sqlite3
database = 'database.sqlite'
conn = sqlite3.connect(database)
print('Opened data successfully')

import pandas as pd
tables = pd.read_sql("""SELECT * 
                    FROM CLASS_10;""", conn)
print(tables)