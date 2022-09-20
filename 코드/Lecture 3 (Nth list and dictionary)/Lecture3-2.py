class_grades = list()
num_students = int(input("학생 수 입력: "))
num_scores = int(input("과목 수 입력: "))

for i in range(num_students):
    tmp_list = list()
    print(i+1, "번째 입니다")
    name = input("학생 이름 입력하세요: ")
    tmp_list.append(name)
    print("개별 과목 점수를 입력합니다.")
    for j in range(num_scores):
        score = input("점수 입력: ")
        tmp_list.append(score)
    class_grades.append(tmp_list)
print(class_grades)