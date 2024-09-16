import sqlite3
database = 'basketball.sqlite'
conn = sqlite3.connect(database)
print('Opened data successfully')

import pandas as pd
teams = pd.read_sql("""SELECT *
                        FROM Team;""", conn)
print(teams)