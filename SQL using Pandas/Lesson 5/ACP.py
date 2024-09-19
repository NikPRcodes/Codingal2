import numpy as np
import pandas as pd
import sqlite3

database = 'basketball.sqlite'
conn = sqlite3.connect(database)
print('Opened data successfully')

all = pd.read_sql("""SELECT *
                FROM Player""", conn)
print(all)

alls = pd.read_sql("""SELECT *
                FROM Player_Salary""", conn)
print(alls)

joined = pd.read_sql("""SELECT DISTINCT ps.namePlayer, ps.nameTeam, ps.value, p.is_active
                     FROM Player_Salary ps
                     Join player p on ps.namePlayer = p.full_name""",conn)
print(joined)