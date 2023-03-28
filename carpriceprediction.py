# -*- coding: utf-8 -*-
"""carpriceprediction

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ORaoiZgWy0BlU-BH5OTIvpovaGARgyCS
"""

# Commented out IPython magic to ensure Python compatibility.
import datetime
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
# %matplotlib inline

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler

#Displaying the starting rows of data
df=pd.read_csv("/carprice.csv")
df.head()

df.isnull().sum()

df.describe()

# Get the unique values in the "CarName" column of the DataFrame "df"
df.CarName.unique()

# Set the plotting style to "darkgrid"
sns.set_style("darkgrid")

# Create a new figure with a size of 15x10 inches
plt.figure(figsize=(15,10))

# Create a histogram of the "price" variable in the DataFrame "df", with a kernel density estimate (KDE) overlaid
sns.distplot(df.price,kde=True)

# Display the plot
plt.show()

corr_matrix = df.corr()
corr_matrix

# Create a new figure with a size of 15x10 inches
plt.figure(figsize=(15,10))

# Compute the correlation matrix
correlation = df.corr()

# Create a heatmap of the correlation matrix
sns.heatmap(correlation, cmap='coolwarm', annot=True)

# Display the plot
plt.show()


#here red indicates positive correlation and blue indicates negative correlation.

df.head()

predict = "price"
data=df[["symboling","wheelbase","carlength","carwidth",
           "carheight","curbweight",
           "enginesize","boreratio","stroke",
           "compressionratio","horsepower",	"peakrpm","citympg","highwaympg","price"]]
x=np.array(data.drop([predict] ,1))
y=np.array(data[predict])

#splitting the data into training and testing data
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size = 0.2)
print(x_train)

print(x_test)

print(y_train)

print(y_test)

from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import accuracy_score

# Create a decision tree regressor
reg = DecisionTreeRegressor()

# Fit the regressor to the training data
reg.fit(x_train, y_train)

# Predict the labels of the test set
y_pred = reg.predict(x_test)

from sklearn.metrics import mean_absolute_error
reg.score(x_test,y_pred)

#prediction
dataset=pd.DataFrame({'Actual' : y_test,'predicted' : y_pred })
dataset

