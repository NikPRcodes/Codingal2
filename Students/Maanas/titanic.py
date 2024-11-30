import pandas as pd
import numpy as np
import seaborn as sb
import matplotlib.pyplot as pt

eda=pd.read_csv('C:/Users/hp/Desktop/Codingal/Students/Maanas/Titanic Dataset.csv')


sb.countplot(eda['Gender'], hue=eda['Survived'])
pt.show()