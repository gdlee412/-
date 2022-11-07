import pandas as pd
import numpy as np

# Seaborn 라이브러리에서 제공하는 타이타닉 데이터를 처리한 데이터입니다.
titanic = pd.read_csv('data/Q2.csv')

###### 코드 #########
Q1 = titanic['fare'].quantile(0.25)
Q3 = titanic['fare'].quantile(0.75)
IQR = Q3 - Q1
df = titanic[titanic['fare'] > (Q3 + 1.5 * IQR)]

print(df['fare'].mean())
