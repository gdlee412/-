# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import numpy as np

########################################코드##########################################
#array size
num = int(input())
# 점수를 담아둘 어레이를 생성하세요
score = np.zeros(num, dtype = int)
# 입력되는 점수 변동 반영을 INPUT_END 입력까지 반복하세요
while True:
	input_string = input()
	if input_string == "INPUT_END":
		break
	else:
		#ask for user input and separate in a list
		user_input = list(map(int, input_string.split()))
		#if first input is in range of the number of students, add the second int to that student's score
		if user_input[0] in range(num):
			score[user_input[0]] += user_input[1]
		#if not part, then just skip
		else:
			continue

# 특정 학생의 점수를 정수로 출력하세요!
score_answer = 0

student_num = int(input())
score_answer = score[student_num]

#####################################################################################
print(int(score_answer))