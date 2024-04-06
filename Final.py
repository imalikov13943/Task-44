import pandas as pd
import random

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})
print("Исходный DataFrame:")
print(data.head())

categories = set(data['whoAmI'])
one_hot_data = pd.DataFrame()
for category in categories:
    one_hot_data[category] = (data['whoAmI'] == category).astype(int)

print("\nDataFrame в one hot виде:")
print(one_hot_data.head())
