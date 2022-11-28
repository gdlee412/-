#Dataframe
import pandas as pd
import numpy as np

df = pd.DataFrame(np.zeros((4,3)))
print(type(df))
#<class 'pandas.core.frame.DataFrame'>

print(df)
#       0       1       2
#0    0.0     0.0     0.0
#1    0.0     0.0     0.0
#2    0.0     0.0     0.0
#3    0.0     0.0     0.0
print()

############################
#Dataframe with labels
classes = ['국어', '영어', '수학']
df = pd.DataFrame(np.zeros((4,3)), columns=classes)
print(type(df))
#<class 'pandas.core.frame.DataFrame'>
print(df)
#      국어     영어      수학
#0    0.0     0.0     0.0
#1    0.0     0.0     0.0
#2    0.0     0.0     0.0
#3    0.0     0.0     0.0

print()
print()

###############################
#Dataframe using dictionary and list

names = ['춘향', '몽룡', '향단', '방자']
korean = [100, 95, 90, 85]
english = [85, 90, 95, 100]
math = [90, 85, 100, 95]

df = pd.DataFrame({'이름':names, '국어':korean, '영어':english, '수학':math})
print(type(df))
#<class 'pandas.core.frame.DataFrame'>
print(df)
#   이름   국어   영어   수학
#0  춘향  100   85   90
#1  몽룡   95   90   85
#2  향단   90   95  100
#3  방자   85  100   95

print(df.columns)
#Index(['이름', '국어', '영어', '수학'], dtype='object')
print(df.index)
#RangeIndex(start=0, stop=4, step=1)
print()

name_ser = df['이름'] #열 인덱스 접근 (column index approach)
print(type(name_ser))
#<class 'pandas.core.series.Series'>
print(name_ser)
#0    춘향
#1    몽룡
#2    향단
#3    방자
#Name: 이름, dtype: object

classes_df = df[['이름','수학']] #열 인덱스 리스트로 접근
print(type(classes_df))
#<class 'pandas.core.frame.DataFrame'>
print(classes_df)
#   이름   수학
#0  춘향   90
#1  몽룡   85
#2  향단  100
#3  방자   95
print()

print(df['영어'])
#0     85
#1     90
#2     95
#3    100
#Name: 영어, dtype: int64

df['영어'] = df['영어'] + 10 #모든 학생에게 보너스 점수
print()
print(df['영어'])
#0     95
#1    100
#2    105
#3    110
#Name: 영어, dtype: int64

###########################
#Accessing Dataframe rows using slicing
#same dataframe as previous one
print()
print()

print(df[1:2])
#   이름  국어   영어  수학
#1  몽룡  95  100  85
print(df[2:])
#   이름  국어   영어   수학
#2  향단  90  105  100
#3  방자  85  110   95
print()

print(df['국어'][1]) #열 접근 먼저
#95
print()
print(df[1:2]['국어']) #행 접근 먼저
#1    95
#Name: 국어, dtype: int64