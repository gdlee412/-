import warnings
warnings.filterwarnings(action='ignore')

# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import numpy as np
import pandas as pd

df = pd.read_csv("data/22_fall_final_train.csv")
#################################코드##################################
df2 = df.copy()

df2.drop(['new_snowfall_3hr', 'cloud_type','lowest_cloud', 'ground_condition', 'wind_direction'], axis = 1, inplace=True)

print(df2.columns)
#################################코드##################################