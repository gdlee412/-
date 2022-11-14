# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import pandas as pd


Korean=[100, 90, 90, 95, 85, 80, 75, 80, 75, 70, 65, 65, 50, 40, 50, 50]
English=[100, 95, 95 ,90, 85, 80, 85, 70, 70, 60, 65, 55, 60, 60, 50, 50]
Math=[100, 90, 95, 85, 80, 70, 60, 70, 85, 80, 95, 45, 80, 85, 50, 75]
Science=[100, 90, 90, 85, 85, 95, 50, 70, 85, 70, 80, 30, 85, 75, 50, 85]
Sports = [100, 100, 80, 100, 100, 90, 70, 60, 80, 95, 70, 70, 85, 95, 95, 100]
Music = [100, 100, 100, 95, 100, 85, 75, 90, 85, 95, 85, 70, 75, 90, 85, 85]
Moral = [100, 85, 75, 85, 90, 100, 85, 75, 90, 85, 100, 100, 75, 90, 95, 60]

##### 코드 ########

scores = pd.DataFrame( {'korean':Korean,'english':English, 'math':Math, 'science':Science, 'sports':Sports, 'music':Music, 'moral':Moral} )

subj_corr = scores.corr()

subj = input()

subj_col = subj_corr[subj]

subj_col = subj_col.drop(subj)

print(subj_col.idxmax(), max(subj_col))
