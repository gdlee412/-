# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import numpy as np
########################################코드##########################################
#array size
size_input = list(map(int, input().split()))
class_size = size_input[0]
student_size = size_input[1]

#create array with the specified size
score = np.zeros((class_size, student_size))

while True:
	input_string = input()
	
	if input_string == "INPUT_END":
		break
	else:
		#split into list
		user_input = input_string.split()
		#simplify names
		group_type = user_input[0]
		class_num = int(user_input[1])
		student_id = int(user_input[2])
		points = int(user_input[3])
		#divide into three different types
		#if group type is STUDENT, give student with the specified class and id the points
		if group_type == "STUDENT":
			score[class_num][student_id] += points
		#elif GROUP, give all students with the id the points
		elif group_type == "GROUP":
			score[:, student_id] += points
		#elif CLASS, give the entire class the points
		elif group_type == "CLASS":
			score[class_num] += points
		else:
			continue

class_score_average = 0.0

class_num = int(input())
#get average of the class
class_score_average = np.mean(score[class_num])
#####################################################################################
print(f"{class_score_average:.2f}")