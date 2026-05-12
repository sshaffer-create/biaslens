import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import f_oneway
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error

#Q1
cars = pd.read_csv("cars.csv")
print(cars.head) #first five rows of cars

#  Q1A
origin_counts = cars.groupby ("Origin").size()
print(origin_counts)
#Q1B
bars = plt.bar(origin_counts.index, origin_counts.values)
plt.show()
#Q1C
missingvalue = cars.isnull().sum()
print(missingvalue)
