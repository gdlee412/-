# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import pandas as pd 

whr = pd.read_csv('data/WHR2022.csv')

####### 코드 #########

data = whr.drop(['Whisker-high', 'Whisker-low', 'Country', 'RANK'], axis = 1)
data.columns = ['happy_score', 'residual', 'gdp', 'social_support', 'health', 'freedom', 'generosity', 'trust']

nums = data.shape[0]
h_border = data.iloc[int(nums/3)]['happy_score']
m_border = data.iloc[int(nums/3) * 2]['happy_score']

def group_rank(x):
  if x >= h_border:
    return 'H'
  elif x >= m_border:
    return 'M'
  else:
    return 'L'

data['group_rank'] = data['happy_score'].apply(group_rank)

data2 = data.groupby('group_rank').mean().sort_values('happy_score', ascending=False)

divided = data2.loc['H'] / data2.loc['L']

divided = divided.sort_values(ascending=False)
print(divided.idxmax(), max(divided))

divided = divided.drop(divided.idxmax())

print(divided.idxmax(), max(divided))