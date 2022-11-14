# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import pandas as pd 

whr = pd.read_csv('data/WHR2022.csv')

####### 코드 ##########

data = whr.drop(['Whisker-high', 'Whisker-low', 'Country', 'RANK'], axis = 1)
data.columns = ['happy_score', 'residual', 'gdp', 'social_support', 'health', 'freedom', 'generosity', 'trust']

data_corr = data.corr()

idx = input()

data_col = data_corr[idx]

data_col = data_col.drop(idx)

print(data_col.idxmax(), max(data_col))
print(data_col.idxmin(), min(data_col))