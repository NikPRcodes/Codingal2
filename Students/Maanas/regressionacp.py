import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error,r2_score

data=pd.read_csv('C:/Users/hp/Desktop/Codingal/Students/Maanas/xydataset.csv')

print(data.shape)

#IndexError: single positional indexer is out-of-bounds
x = data.iloc[:, :-1].values
y = data.iloc[:, -1].values


xtrain = x[:-20] 
xtest = x[-20:]  
ytrain = y[:-20] 
ytest = y[-20:]

regr=linear_model.LinearRegression()
regr.fit(xtrain,ytrain)

ypred=regr.predict(xtest)

print('coefficients',regr.coef_)
print('mean squared error: %.2f'%mean_squared_error(ytest,ypred))
print('coefficient of determination %.2f' %r2_score(ytest,ypred))

plt.scatter(xtest,ytest,color='black')
plt.plot(xtest,ypred,color='blue',linewidth=3)
plt.xticks(())
plt.yticks(())
plt.show()