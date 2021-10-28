import pandas as pd
from pandas.core.frame import DataFrame

DataFrame = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv')

print("-----------------------------------------------------")

mediaSetosa = DataFrame.loc[DataFrame['species'] == 'setosa', 'petal_length'].mean()
print("Media da espécie Setosa:")
print(mediaSetosa)

print("-----------------------------------------------------")

mediaVirginica = DataFrame.loc[DataFrame['species'] == 'virginica', 'petal_length'].mean()
print("Media da espécie Virginica:")
print(mediaVirginica)

print("-----------------------------------------------------")

mediaVersicolor = DataFrame.loc[DataFrame['species'] == 'versicolor', 'petal_length'].mean()
print("Media da espécie Versicolor:")
print(mediaVersicolor)

print("-----------------------------------------------------")

