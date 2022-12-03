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
#for example
#date = '2022-01-01 01:00'
#month = date_time_split(date)
#print(month)

df2 = df.copy()

df2['month'] = df2['date_time'].apply(date_time_split)

want_month = int(input())

df3 = df2[df2['month'] == want_month]

print(len(df3.index))
#################################코드##################################
