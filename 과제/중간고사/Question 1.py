score_0_list = [96, 67, 74, 72, 74, 100, 61, 66, 88, 85, 83, 85, 68, 53, 50, 22, 65, 78, 70, 64, 65, 100, 65, 86, 86, 87, 64, 70, 76, 75, 77, 75, 62, 100, 41, 56, 86, 87, 85, 53, 74, 100, 93, 40, 80, 58, 74, 61, 84, 55, 84, 72, 49, 70, 100, 63, 80, 77, 73, 96, 86, 74, 95, 88, 65, 73, 86, 74, 73, 50, 46, 95, 91, 82, 84, 100, 76, 92, 77, 54, 54, 82, 80, 73, 56, 63, 79, 78, 88, 73, 64, 92, 60, 85, 97, 83, 72, 95, 88, 73]
score_1_list = [52, 67, 97, 67, 67, 60, 63, 75, 51, 76, 63, 58, 80, 77, 66, 88, 68, 49, 95, 70, 73, 47, 84, 73, 48, 87, 63, 100, 75, 48, 59, 71, 86, 31, 40, 67, 44, 48, 77, 40, 73, 45, 64, 63, 61, 12, 59, 70, 68, 77, 64, 45, 92, 88, 68, 88, 39, 88, 79, 56, 78, 55, 82, 100, 93, 36, 53, 66, 49, 74, 41, 64, 89, 58, 61, 59, 62, 62, 76, 54, 94, 19, 66, 78, 57, 75, 63, 49, 73, 49, 34, 52, 57, 63, 59, 69, 69, 68, 77, 53]
score_2_list = [87, 90, 55, 76, 59, 55, 51, 79, 54, 34, 46, 38, 34, 11, 75, 55, 59, 42, 21, 100, 90, 54, 63, 87, 92, 71, 55, 73, 86, 86, 43, 93, 87, 60, 71, 80, 83, 77, 84, 66, 82, 61, 87, 83, 72, 38, 67, 67, 71, 70, 99, 27, 81, 100, 52, 61, 74, 80, 41, 71, 40, 55, 66, 50, 93, 71, 75, 60, 49, 76, 68, 41, 28, 55, 60, 56, 66, 42, 78, 64, 66, 56, 63, 91, 86, 59, 42, 82, 59, 57, 74, 61, 55, 79, 66, 66, 63, 82, 100, 86]

# 아래 세 변수는, 리스트 자료형으로 주어진 데이터입니다.
# 아래 변수들을 이용하여 문제를 해결하세요.
score_0 = score_0_list
score_1 = score_1_list
score_2 = score_2_list
#receive input
score_0_pass = int(input())
score_1_pass = int(input())
score_2_pass = int(input())

#find number of students
class_size = len(score_0)

#initialize a list with 0s to save passing subjects
passing_list = [0 for _ in range(class_size)]

#find number of subjects a student passed
for i in range(class_size):
	if score_0[i] >= score_0_pass:
		passing_list[i] += 1
	if score_1[i] >= score_1_pass:
		passing_list[i] += 1
	if score_2[i] >= score_2_pass:
		passing_list[i] += 1

#num of passing students
num_of_passing_students = 0
for i in range(class_size):
	if passing_list[i] == 3:
		num_of_passing_students += 1
		
print(num_of_passing_students)