import pandas as pd
import numpy as np
import matplotlib.pyplot as pt
import seaborn as sb

perf=pd.read_csv('C:/Users/hp/Desktop/Codingal/Students/Maanas/StudentsPerformance.csv')
print(perf.isnull().sum())
print(perf.describe())

perf.groupby('parental level of education').size().plot(kind='pie',autopct='%.2f')
pt.show()   
perf.groupby('race/ethnicity').size().plot(kind='pie',autopct='%.2f')
pt.show()   
#Help 6
pt.bar(data=perf,x='race/ethnicity',height='gender')
pt.show()   
#Help 7
sb.scatterplot(data=perf, x='gender',hue='lunch')
pt.show() 

sb.boxplot()