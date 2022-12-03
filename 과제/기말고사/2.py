import warnings
warnings.filterwarnings(action='ignore')

# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import numpy as np
import pandas as pd

df = pd.read_csv("data/22_fall_final_train_after_q1.csv")
#################################코드##################################
df2 = df.copy()

int_input = int(input())
col = input()

df3 = df2[df2['humidity'] < 60]

print(df3[col].median())
#################################코드##################################
