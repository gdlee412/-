import warnings
warnings.filterwarnings(action='ignore')

# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import numpy as np
import pandas as pd

df = pd.read_csv("data/22_fall_final_train.csv")
#################################코드##################################
df2 = df.copy()

col = input()

df2[col].fillna(0, inplace=True)

print(df2[col].mean().round(2))
#################################코드##################################