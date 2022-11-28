import pandas as pd

#loc -> 2차원 인덱싱

#iloc => 정수 기반의 2차원 인덱싱

names = ['춘향', '몽룡', '향단', '방자']
korean = [100, 95, 90, 85]
english = [85, 90, 95, 100]
math = [90, 85, 100, 95]

df = pd.DataFrame({'국어':korean, '영어':english, '수학':math}, index=names)
print(df)
#     국어   영어   수학
#춘향  100   85   90
#몽룡   95   90   85
#향단   90   95  100
#방자   85  100   95
print()

print(df.loc['춘향']) #행 접근
#국어    100
#영어     85
#수학     90
#Name: 춘향, dtype: int64
print()

print(df.loc[['춘향', '향단']]) #행 리스트 접근
#     국어  영어   수학
#춘향  100  85   90
#향단   90  95  100
print()

print(df.loc['춘향','국어']) #개별 값 접근
#100
print()

print(df.loc['몽룡':'방자']) #슬라이스의 마지막 값이 포함된다
#    국어   영어   수학
#몽룡  95   90   85
#향단  90   95  100
#방자  85  100   95
print()

print(df.loc[df['국어'] > 90]) #불리언 시리즈 접근
#     국어  영어  수학
#춘향  100  85  90
#몽룡   95  90  85
print()

print(df.loc[['춘향', '몽룡'],['수학','영어']]) #행과 열 모두 리스트로 접근
#    수학  영어
#춘향  90  85
#몽룡  85  90
print()

print(df.loc[df['수학'] > 90, ['국어', '영어']]) #수학 90점 넘는 학생의 국어 영어 점수
#    국어   영어
#향단  90   95
#방자  85  100


#####################################
#iloc 사용
print(df)
print()

print(df.iloc[0]) #한 행 접근
#print(df.loc['춘향'])
#국어    100
#영어     85
#수학     90
#Name: 춘향, dtype: int64
print()

print(df.iloc[[0, 2]]) #한 행 접근
#print(df.loc[['춘향', '향단']])
#     국어  영어   수학
#춘향  100  85   90
#향단   90  95  100
print()

print(df.iloc[0,0])#단일 값 접근
#print(df.loc['춘향','국어'])
#100
print()

print(df.iloc[0:2]) #행 슬라이싱
#print(df.loc['춘향':'몽룡'])
#     국어  영어  수학
#춘향  100  85  90
#몽룡   95  90  85
print()

print(df.iloc[0:2, 1:3]) #행과 열 슬라이싱
#    영어  수학
#춘향  85  90
#몽룡  90  85
print()

print(df.iloc[[0,3],[1,2]]) #행과 열 리스트 접근
#print(df.loc[['춘향', '방자'],['영어','수학']])
#     영어  수학
#춘향   85  90
#방자  100  95
print()

print(df.iloc[0] > 90) #불리언 시리즈
#국어     True
#영어    False
#수학    False
#Name: 춘향, dtype: bool
print()

print(df.iloc[0][df.iloc[0] > 90]) #행렬 인덱스 0 학생 점수 중 90점 넘는 것
#국어    100
#Name: 춘향, dtype: int64