# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import numpy as np
import pandas as pd

def slice_col_name(col_name):
    return int(col_name[:2])

df = pd.read_csv('./data/line1_kb.csv')
a, b, c = map(int, input().split())


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
start_work = 0
#use for loop to find the time with the least entering customers
for i in range(a, b - c):
	temp_total = time_list[i] + time_list[i + 1 + c]
	if total > temp_total:
		total = temp_total
		start_work = i
		
#print best case
print(start_work, " ", start_work + 1, " ", start_work + 1 + c)