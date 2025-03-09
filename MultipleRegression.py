import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
from dask.array import reshape
from pandas import read_csv,read_excel,read_stata

dataset = pd.read_csv("50_Startups.csv")

x = dataset.iloc[ : , :-1].values
y = dataset.iloc[ : , -1].values

from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
ct = ColumnTransformer(transformers=[("encoder",OneHotEncoder(),[3])],remainder="passthrough")
x = ct.fit_transform(x)
print(x)