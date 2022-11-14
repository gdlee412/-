# -*- coding: utf-8 -*# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import numpy as np
import pandas as pd

##### 코드 #######
# 1. 데이터 읽어오기
df_p = pd.read_csv("data/air_pollution.csv")
df_w = pd.read_csv("data/weather.csv")

# 2. 데이터프레임 Merge
df = pd.merge(df_p, df_w)

# 3. 미세먼지/초미세먼지 이상치 제거
PM_idx = df[df['PM10'] >= 500].index
df.drop(PM_idx, inplace=True)
PM_idx = df[df['PM2.5'] >= 500].index
df.drop(PM_idx, inplace=True)

# 4. 결측치 제거
df.dropna(inplace=True)

# 5. 인덱스 초기화
df.reset_index(inplace=True, drop=True)

def PM10rank(x):
	if x >= 75:
		return '매우나쁨'
	elif x >= 35:
		return '나쁨'
	elif x >= 15:
		return '보통'
	else:
		return '좋음'

df['PM2.5 Level'] = df['PM2.5'].apply(PM10rank)

groupbyed_mean_df = df.groupby('PM2.5 Level').mean().sort_values('PM2.5', ascending=True) # 초미세먼지 등급 기준 groupby 평균치 결과


#########
column_name = input()
print(groupbyed_mean_df.loc[['좋음', '보통', '나쁨', '매우나쁨'] ,column_name])