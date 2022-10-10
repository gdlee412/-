import pandas as pd
import numpy as np
file_path = 'data/score_4.csv' # 파일 경로
score_4 = pd.read_csv(file_path)

file_path_attend = 'data/attend.csv'
attend = pd.read_csv(file_path_attend)

pd.set_option('mode.chained_assignment',  None)

##여기에 코드를 작성하세요##
score_4 = pd.merge(score_4, attend)
score_4 = score_4.sort_values('평균', ascending = False)
score_5 = score_4[['이름', '출석율']]
print('평균 점수 상위 3명의 출석율')
print(score_5.head(3))
print()

print('평균 점수 하위 3명의 출석율')
print(score_5.tail(3))
print()

score_4 = score_4.sort_values('출석율', ascending = False)
score_5 = score_4[['이름', '평균']]
print('출석율 상위 3명의 평균 점수')
print(score_5.head(3))
print()

print('출석율 하위 3명의 평균 점수')
print(score_5.tail(3))
#########################