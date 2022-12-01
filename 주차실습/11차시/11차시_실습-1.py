import pandas as pd
import numpy as np

# Seaborn 라이브러리에서 제공하는 타이타닉 데이터 입니다.
titanic = pd.read_csv('data/Q0.csv')

########################################코드##########################################

def encoding(x):
  if x == 'male':
    return 0
  else:
    return 1

titanic = titanic[['survived', 'sex', 'fare', 'age', 'embarked']]

titanic.dropna(inplace=True)
titanic.drop_duplicates(inplace=True)
titanic['sex_code'] = titanic['sex'].apply(encoding)
titanic.reset_index(inplace=True, drop=True)

print(titanic)

# 살짝 다른 방식
# df = titanic.copy()

# df = df[['survived', 'sex', 'fare', 'age', 'embarked']]

# df.drop_duplicates(inplace=True)
# df.dropna(inplace=True)

# def encoding(x):
# 	if x == "male":
# 		return 0
# 	else:
# 		return 1
	
# df['sex_code'] = df['sex'].apply(encoding)

# df.reset_index(inplace=True,drop=True)

# print(df)
#####################################################################################