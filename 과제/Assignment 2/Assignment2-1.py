# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import numpy as np
import pandas as pd


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

# 결과 출력
idx = int(input())
print(df.iloc[idx])