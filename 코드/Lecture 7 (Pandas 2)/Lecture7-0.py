import pandas as pd

names = ['춘향', '몽룡', '향단', '방자']
korean = [100, 95, 90, 85]
english = [85, 90, 95, 100]
math = [90, 85, 100, 95]

df= pd.DataFrame({'국어':korean, '영어':english, '수학':math}, index = names)
print(df)
print()
#     국어   영어   수학
#춘향  100   85   90
#몽룡   95   90   85
#향단   90   95  100
#방자   85  100   95

df.loc['학도'] = {'국어': 50, '영어': 50, '수학': 5} #행 추가
print(df)
print()
#     국어   영어   수학
#춘향  100   85   90
#몽룡   95   90   85
#향단   90   95  100
#방자   85  100   95
#학도   50   50    5

df.drop('학도', axis = 0, inplace = True) #행 삭제, axis = 0 행 방향으로 의미
#inplace =  True는 삭제를 현재 데이터프레임 내에 반영하라는 의미
print(df)
#     국어   영어   수학
#춘향  100   85   90
#몽룡   95   90   85
#향단   90   95  100
#방자   85  100   95


df['체육'] = [100,100,100,100] #열 추가
print(df)
print()
#    국어   영어   수학   체육
#춘향  100   85   90  100
#몽룡   95   90   85  100
#향단   90   95  100  100
#방자   85  100   95  100

df.drop('체육', axis = 1, inplace = True) 
print(df)
print()
#     국어   영어   수학
#춘향  100   85   90
#몽룡   95   90   85
#향단   90   95  100
#방자   85  100   95

print(df['국어'].count()) #국어 열의 데이터 개수
#4
print(df.count()) #각 열마다 데이터 개수
#국어    4
#영어    4
#수학    4
#dtype: int64

print(df['수학'].value_counts()) #각 데이터가 나온 개수
print()
#90     1
#85     1
#100    1
#95     1
#Name: 수학, dtype: int64

print(df['영어'].sort_index())#그 열의 데이터
#몽룡     90
#방자    100
#춘향     85
#향단     95
#Name: 영어, dtype: int64
print(df['영어'].sort_values()) #그 열의 데이터를 오름차순으로
print()
#춘향     85
#몽룡     90
#향단     95
#방자    100
#Name: 영어, dtype: int64

print(df.sort_values('영어')) #그 열의 오름차순으로 배열을 바꾼다
#     국어   영어   수학
#춘향  100   85   90
#몽룡   95   90   85
#향단   90   95  100
#방자   85  100   95

print(df.sort_values(['영어', '수학'])) #첫 열로 정리한다, 하지만 같은 수가 만약의 존재하면 두번째 열로 정리한다