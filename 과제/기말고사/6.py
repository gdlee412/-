# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import warnings
import pandas as pd
import numpy as np

warnings.filterwarnings('ignore')

# 채점을 위한 함수입니다.
def calculate_score(train_score, test_score, target_score):
	print(f"Train Score: {train_score:.4f}, Test Score: {test_score:.4f}  -  ", end="")
	
	if test_score > target_score and train_score > target_score:
		print("Passed")
	else:
		print("Failed")

# csv 파일을 다음과 같이 불러옵니다.
train_df = pd.read_csv('data/22_fall_final_train.csv')
test_df = pd.read_csv('data/22_fall_final_test.csv')

# 활동지수가 0보다 클지를 맞춰야 합니다.
train_y = train_df['activity_score'] > 0.0
train_df = train_df.drop(['activity_score'],axis = 1)
test_y = test_df['activity_score'] > 0.0
test_df = test_df.drop(['activity_score'],axis = 1)
#################################코드##################################
# 파생변수 추가
train_df.fillna(0, inplace=True)
test_df.fillna(0, inplace=True)

from sklearn.linear_model import LogisticRegression

train_X = train_df.drop(['station_name', 'date_time', 'new_snowfall_3hr', 'cloud_type','lowest_cloud', 'ground_condition', 'wind_direction'],axis=1)  # 설명변수 선택
test_X = test_df.drop(['station_name', 'date_time', 'new_snowfall_3hr', 'cloud_type','lowest_cloud', 'ground_condition', 'wind_direction'],axis=1)  # 설명변수 선택

lr = LogisticRegression()  # scikit-learn 로지스틱 회귀 모델 학습

lr.fit(train_X, train_y)
#################################코드##################################
target_score = float(input())

calculate_score(
	lr.score(train_X, train_y),
	lr.score(test_X, test_y),
	target_score
)