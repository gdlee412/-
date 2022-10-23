#dont forget "pip install pandas"
import pandas as pd

#creating a series
ser = pd.Series([10, 20, 30, 40])
print(type(ser))
#<class 'pandas.core.series.Series'>

print(ser)
#0      10
#1      20
#2      30
#3      40
#dtype: int64

print()
print(ser[0], ser[2])
#10 30

print(ser.index)
#RangeIndex(start=0, stop=4, step=1)

print()

grades = ['A', 'B+', 'A+', 'A']
ser = pd.Series(grades, index = ['춘향', '몽룡', '향단', '방자'])
print(type(ser))
#<class 'pandas.core.series.Series>

print(ser)
#춘향       A
#몽룡       B+
#향단       A+
#방자       A
#dtype: object
print()

print(ser[0],ser[2])
#A A+
print(ser['춘향'],ser['향단'])
#A A+
print(ser.index)
#Index(['춘향','몽룡',향단','방자'], dtype='object')