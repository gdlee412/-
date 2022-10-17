# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import numpy as np
import pandas as pd

def slice_col_name(col_name):
    return int(col_name[:2])

df = pd.read_csv('./data/line1_kb.csv')
a, b = map(int, input().split())


#create series with only the time and number of customers
sum_col = df.sum(axis=0)
sum_col = sum_col.drop(labels = ['지하철역', '작업일자'])
length = len(sum_col)

#empty dictionary
time_list = {}

#create a dictionary with the hours only
for index in sum_col.index:
	#tempindex name for the hour
	tempindex = slice_col_name(index)
	#if the index is already existent, then the current index will represent the exiting customers (하차)
	#so ignore
	if tempindex in time_list:
		continue
	#otherwise, it will represent the entering customers(승차)
	else:
		time_list[tempindex] = sum_col[index]

total = 100000000
best_index = 0
#use for loop to find the time with the least entering customers
for i in range(a, b + 1):
	if total > time_list[i]:
		total = time_list[i]
		best_index = i

#print best case
print(best_index)