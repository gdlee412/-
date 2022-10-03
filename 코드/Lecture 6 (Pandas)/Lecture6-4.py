### CSV 파일 사용 ###

import pandas as pd

#replace filename.csv with the csv file
df = pd.read_csv("filename.csv")
print(df)

print(df.head()) #첫 5개의 데이터
print(df.head(10)) #첫 10개의 데이터

print(df.tail()) #마지막 5개의 데이터
print(df.tail(10)) #마지막 10개의 데이터

print(df.index) #행 인덱스 확인

print(df.columns) #열 레이블

print(df.describe()) #열마다의 통계적 데이터

res = df.describe()
print(type(res))
#<class 'pandas.core.frame.DataFrame'>

print(res.loc['mean']) #열마다의 mean 출력

print(res.loc['mean']['PetalWidth']) #특정 열의 mean 접근