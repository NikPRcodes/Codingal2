import sqlite3
database = 'database.sqlite'
conn = sqlite3.connect(database)
print('Opened data successfully')

import pandas as pd
MI_S8_S9 = pd.read_sql("""SELECT *
                        FROM Match
                        WHERE Match_Winner == 7 and Season_Id IN (8,9);""", conn)
print(MI_S8_S9)

new_teams = pd.read_sql("""SELECT *
                        FROM Team
                        WHERE Team_Name LIKE 'De%';""", conn)
print(new_teams)

# Check the minimum and maximum win_margin of all the matches 
min_max_margin = pd.read_sql("""SELECT MIN(Win_Margin), MAX(Win_Margin)
                        FROM Match;""", conn)
print(min_max_margin)