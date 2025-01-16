import pandas as pd

# Create dictionary with the given data
data = {
    'Id': [1, 2, 3, 4],
    'Name': ['Pankaj', 'Meghna', 'David', 'Lisa'],
    'Role': ['CEO', 'Manager', None, 'Assistant'],
    'Salary': [100, 200, None, None]
}

# Create DataFrame
df = pd.DataFrame(data)

# Print the initial 2 and last 2 rows
#print("Initial 2 and Last 2 rows:\n", df.head(2).append(df.tail(2)))
print("Initial 2 and Last 2 rows:\n", df.head(2), (df.tail(2)))
# Check the total number of null values in the DataFrame
print("\nTotal null values:", df.isnull().sum().sum())
# Print detailed information of the DataFrame
df.info()
# Drop all rows with null values and store in a new DataFrame
df_no_null_rows = df.dropna()
print("\nDataFrame after dropping rows with null values:\n", df_no_null_rows)

# Drop all columns with null values and store in a new DataFrame
df_no_null_columns = df.dropna(axis=1)
print("\nDataFrame after dropping columns with null values:\n", df_no_null_columns)

# Fill null values in Salary column with 300
df['Salary'] = df['Salary'].fillna(300)
print("\nDataFrame after filling null values in Salary with 300:\n", df)

# Fill null values in Role column with 'CEO'
df['Role'] = df['Role'].fillna('CEO')
print("\nDataFrame after filling null values in Role with 'CEO':\n", df)