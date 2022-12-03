import warnings
warnings.filterwarnings(action='ignore')

# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import numpy as np
import pandas as pd

df = pd.read_csv("data/22_fall_final_train_after_q1.csv")

def date_time_split(data) : #(dataframe or string)을 변수로 받습니다.
  if isinstance(data, pd.core.frame.DataFrame) :
    month_data = data.date_time.str[5:7].astype('int32')
  if isinstance(data, str) :
    month_data = int(data[5:7])
  return month_data

#################################코드##################################
df2 = df.copy()

df2['month'] = df2['date_time'].apply(date_time_split)

want_month = int(input())
want_rank = int(input())

df2 = df2[df2['month'] == want_month]

gb = df2.groupby(df2['station_name']).mean()

gb = gb.sort_values(by='activity_score', ascending=False)

print(list(gb.index)[want_rank - 1])
#################################코드##################################