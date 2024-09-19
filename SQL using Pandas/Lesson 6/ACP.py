import pandas as pd
import numpy as np
import sqlite3

database = 'basketball.sqlite'
conn = sqlite3.connect(database)

team = pd.read_sql("""SELECT *
                FROM Team""", conn)
print(team)

teamAttr = pd.read_sql("""SELECT *
                FROM Team_Attributes""", conn)
print(teamAttr)

joined = pd.read_sql("""SELECT *
                FROM Team_Attributes ta
                LEFT JOIN TEAM t ON ta.ID = t.id
                WHERE t.city = 'New York'""", conn)
print(joined)