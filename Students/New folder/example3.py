import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv("C:/Users/hp/Desktop/Codingal/Students/New folder/penguins_size.csv")
print(sns.get_dataset_names())
print(df.head(10))
print(df.shape)
print(df.tail())
print(df.isnull().sum())
print(df.describe())
print(df.describe().T)
print(df.describe(include='all'))
print(df.dtypes)
print(df.info())
df2=df.select_dtypes("float64")
print(df2.corr())
sns.heatmap(df2.corr(), cmap= 'Wistia', annot=True)
df.hist(figsize=(12,8))
plt.show()
df.plot(kind= 'box', subplots=True, layout=(3,2), sharex=False, sharey= False , figsize=(8,12))
plt.show()
print(df.sex.value_counts())
print(df.island.value_counts())
print(df.species.value_counts())
sns.countplot(data=df, x='sex', palette='summer')
plt.show()
sns.countplot(data=df, x='island', palette='RdPu')
plt.show()
sns.countplot(data=df, x='species', palette='YlOrRd')
plt.show()
sns.countplot(data= df, x='sex', palette='rocket', hue='species')
plt.show()
sns.countplot(data= df, x= 'island', hue='species', palette='husl')
plt.show()
sns.countplot(data= df, x= 'island', hue='sex', palette='spring')
plt.show()
sns.pairplot(data=df, hue='species',palette='mako')
plt.show()