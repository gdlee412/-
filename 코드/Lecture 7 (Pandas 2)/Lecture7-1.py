import numpy as np
import pandas as pd

df = pd.DataFrame(np.random.randint(10, size = (3, 6)))
print(df)
print()

print(df.sum()) #방향 없으면 axis = 0 가 기본
print()
print(df.sum(axis = 1)) #한 행을 더한다 sum of a row

df2 = df[df > df.mean()]
print(df2)
#values greater than mean

d1 = pd.DataFrame(np.zeros(6).reshape(3,2), index=['a','b','c'], columns=['v1','v2'])
d2 = pd.DataFrame(np.zeros(4).reshape(2,2), index = ['a','c'], columns=['v1','v2'])
print(d1)
#    v1   v2
#a  0.0  0.0
#b  0.0  0.0
#c  0.0  0.0
print(d2)
#    v1   v2
#a  0.0  0.0
#c  0.0  0.0
print()

print(pd.concat([d1,d2], axis = 0)) #행 방향으로 합치기 combine using columns
print()
#    v1   v2
#a  0.0  0.0
#b  0.0  0.0
#c  0.0  0.0
#a  0.0  0.0
#c  0.0  0.0
print(pd.concat([d1,d2], axis = 1)) #열 방향으로 합치기 combine using rows
#    v1   v2   v1   v2
#a  0.0  0.0  0.0  0.0
#b  0.0  0.0  NaN  NaN
#c  0.0  0.0  0.0  0.0

d3 = pd.merge(d1, d2) #공통점을 이용하여 합친다
print(d3)
#    v1   v2
#0  0.0  0.0
#1  0.0  0.0
#2  0.0  0.0
#3  0.0  0.0
#4  0.0  0.0
#5  0.0  0.0