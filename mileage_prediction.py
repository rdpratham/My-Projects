# -*- coding: utf-8 -*-
"""Mileage_Prediction.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1-j4eHLQz6d_SjTgjLqd8lUgUs-A5MQ63
"""

import pandas as pd

df= pd.read_csv('https://github.com/YBI-Foundation/Dataset/raw/main/MPG.csv')

df.head()

df.columns

import seaborn as sns
sns.pairplot(df,x_vars=['cylinders','displacement','horsepower','weight','acceleration','model_year','origin','name'],y_vars=['mpg'])

df.columns

"""After Visualisation we can say that Cylinders,Model_year,name and origin has no effect on mpg
So we continue with remaining attributes
"""

ndf= df.drop(['cylinders','model_year','name','origin'],axis=1)

ndf.columns

ndf.shape

ndf.isnull().sum()

import numpy as np

ndf['horsepower']=ndf['horsepower'].fillna(np.mean(ndf['horsepower']))

ndf.isnull().sum()

ndf.shape

y = ndf['mpg']

x = ndf.drop(['mpg'],axis=1)

x.shape

x.columns

"""First Creating Model Without Standard Scaler"""

from sklearn.model_selection import train_test_split

x_test,x_train,y_test,y_train=train_test_split(x,y,random_state=2529)

from sklearn.linear_model import LinearRegression
md = LinearRegression()

md.fit(x_train,y_train)

y_p = md.predict(x_test)

y_p

from sklearn.metrics import mean_absolute_error , r2_score

mean_absolute_error(y_p,y_test)

r2_score(y_p,y_test)

"""Now Creating with Standard Scaler"""

x.shape

from sklearn.preprocessing import StandardScaler
sc= StandardScaler()

x = sc.fit_transform(x)

x

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,random_state=2529)

from sklearn.linear_model import LinearRegression
lr = LinearRegression()

lr.fit(x_train,y_train)

y_pr=lr.predict(x_test)

from sklearn.metrics import mean_absolute_error,r2_score

mean_absolute_error(y_pr,y_test)

r2_score(y_pr,y_test)





