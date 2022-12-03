import warnings
warnings.filterwarnings(action='ignore')

# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import numpy as np
import pandas as pd

df = pd.read_csv("data/22_fall_final_train_after_q1.csv")
#################################코드##################################
df2 = df.copy()

def encoded_temp(x):
	return abs(x - 15)

df2['derivated_temp'] = df2['temperature'].apply(encoded_temp)
df2['derivated_solar'] = np.sign(df2['temperature'] - 15) * df2['solar_radiation']

corr = df2.corr()

print(round(corr['temperature']['derivated_temp'], 2))
print(round(corr['temperature']['derivated_solar'], 2))
#################################코드##################################