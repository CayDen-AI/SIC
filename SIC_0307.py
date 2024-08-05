import pandas as pd
import numpy as np
import scipy.stats as st



## data_iris
df = pd.read_csv('./data/data_iris.csv')
print(df.head())
print(df.shape)

## pearson
x = df['Petal.Length']
y = df['Sepal.Length']
print("pearson:", np.round(st.pearsonr(x, y), 3))
print(x.corr(y))
# print(np.round(df.corr(), 3))
# print(df.corr())
print(df['Species'].unique())

df1 = df.copy()
df1.Species.replace({
    'setosa': 0,
    'versicolor': 1,
    'virginica': 2,
}, inplace=True)
print(df1.head())

print(np.round(df1.corr(), 3))

## pearman
print("pearman:", np.round(st.spearmanr(x, y), 3))

## kendall
print("kendall:", np.round(st.kendalltau(x, y), 3))



## data_studentlist
df = pd.read_csv('./data/data_studentlist.csv')
print(df.head())

x = df.height
y = df.weight
n = len(x)
r = x.corr(y)
z = np.arctanh(r)
std_error_z = 1 / np.sqrt(n - 3)

first = {'low': np.tanh(z - st.norm.ppf(0.975) * std_error_z), 'high': np.tanh(z + st.norm.ppf(0.975) * std_error_z)}
second = {'low': np.tanh(z - st.norm.ppf(0.995) * std_error_z), 'high': np.tanh(z + st.norm.ppf(0.995) * std_error_z)}
print(first)
print(second)
