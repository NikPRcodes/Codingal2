import sqlite3
database = 'database.sqlite'
conn = sqlite3.connect(database)
print('Opened data successfully')

import pandas as pd
matches = pd.read_sql("""SELECT *
                        FROM Match;""", conn)

# Print Table info
print(matches.info())

