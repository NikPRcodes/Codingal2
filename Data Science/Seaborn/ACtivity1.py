import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv(r'C:\Users\hp\Desktop\Codingal\Data Science\Seaborn\USA_Housing.csv')
df.head(10)

df.info()
df.describe()
df.columns
sns.pairplot(df)
#sns.heatmap(df.corr(),annot=True)
# Select only numeric columns
numeric_df = df.select_dtypes(include=['float64', 'int64'])

# Compute the correlation matrix and plot heatmap
corr_matrix = numeric_df.corr()
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
plt.show()