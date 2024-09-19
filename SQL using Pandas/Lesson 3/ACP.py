import sqlite3
database = 'database.sqlite'
conn = sqlite3.connect(database)
print('Opened data successfully')

import pandas as pd

tables = pd.read_sql("""SELECT DISTINCT(Man_of_the_Match)  
                    FROM Match;""", conn)
print(tables)