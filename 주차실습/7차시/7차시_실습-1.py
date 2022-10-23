import pandas as pd
file_path = 'data/score_1.csv' # 파일 경로
pd.set_option('mode.chained_assignment',  None)
score_1 = pd.read_csv(file_path)

print('원본 점수표')
print(score_1)

##여기에 코드를 작성하세요##

score_2 = score_1[score_1['역사'] >= 60]

#교수님 코드 
#index = score_1[score_1['역사'] < 60].index
#score_1.drop(index, inplace=True)

print('과락 반영 점수표')
print(score_2)
#########################