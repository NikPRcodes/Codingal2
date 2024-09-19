import numpy as np
import pandas as pd
import sqlite3

database = 'database.sqlite'
conn = sqlite3.connect(database)
print('Opened data successfully')

joined_city = pd.read_sql("""SELECT c.Country_Id, c.Country_Name, ci.City_Name
                            FROM Country as c
                            INNER JOIN city as ci
                            ON c.Country_Id == ci.Country_id""", conn)
print(joined_city)

# Check how Outer join works
joined_left = pd.read_sql("""SELECT *
                            FROM player
                            LEFT JOIN season
                            ON player.Player_Id == season.Man_of_the_Series""", conn)
print(joined_left)

# Check how Cross join works
joined_cross = pd.read_sql("""SELECT c.Country_Id, c.Country_Name, ci.City_Name
                            FROM country c
                            CROSS JOIN city ci""", conn)
print(joined_cross)

# Check how Union Clause works
union = pd.read_sql("""SELECT Player_Name 
                      FROM player
                      UNION
                      SELECT Team_Name
                      FROM Team""", conn)
print(union)