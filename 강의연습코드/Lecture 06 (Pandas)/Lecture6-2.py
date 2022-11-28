import pandas as pd

names = ['춘향', '몽룡', '향단', '방자']
korean = [100, 95, 90, 85]
english = [85, 90, 95, 100]
math = [90, 85, 100, 95]

df = pd.DataFrame({'국어':korean, '영어':english, '수학':math}, index=names)
print(type(df))
#<class 'pandas.core.frame.DataFrame'>
print(df)
#     국어   영어   수학
#춘향  100   85   90
#몽룡   95   90   85
#향단   90   95  100
#방자   85  100   95
print()

#################################
#using boolean for indexing
bool_index = df['수학'] > 90
print(bool_index)
#춘향    False
#몽룡    False
#향단     True
#방자     True
#Name: 수학, dtype: bool
print()
print(df[bool_index]) #boolean true인 인덱스만 부른다
#   국어   영어   수학
#향단  90   95  100
#방자  85  100   95
print()

bool_index = df > 90
print(bool_index)
#       국어     영어     수학
#춘향   True  False  False
#몽룡   True  False  False
#향단  False   True   True
#방자  False   True   True
print()
print(df[bool_index])
       국어     영어     수학
#춘향  100.0    NaN    NaN
#몽룡   95.0    NaN    NaN
#향단    NaN   95.0  100.0
#방자    NaN  100.0   95.0