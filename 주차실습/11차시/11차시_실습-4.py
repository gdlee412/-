import pandas as pd
import numpy as np

# Seaborn 라이브러리에서 제공하는 타이타닉 데이터를 처리한 데이터입니다.
titanic = pd.read_csv('data/Q3.csv')

########################################코드##########################################
# 여기에서 데이터를 처리하세요
male_adult = titanic[titanic['adult_male'] == True]
min = male_adult['age'].min()

def adult(x):
	if x >= min:
		return 1
	else:
		return 0
	
titanic['adult'] = titanic['age'].apply(adult)

processed_data = titanic

#####################################################################################
# 이 부분은 processed_data 변수를 이용해 출력값을 내는 부분입니다.
# 채점은 이 부분을 활용하여 진행되니 다른 출력값을 내지 마세요.

print(processed_data['adult'].value_counts())