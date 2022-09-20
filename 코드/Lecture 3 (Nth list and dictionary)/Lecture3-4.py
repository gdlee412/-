students = dict()
students[2022001] = ['이순신', '군사전략학과']
students[2022002] = ['잭바우어', '경호학과']
print(students)
print(students[2022001])
st = students[2022001]
print(st[0], st[1])
print()

students1 = dict()
students1[2022001] = {'이름': '이순신', '학과': '군사전략학과'}
students1[2022002] = {'이름': '잭바우어', '학과': '경호학과'}
print(students1)
print(students1[2022002])
st = students1[2022002]
print(st['이름'], st['학과'])
print()
for key in students1:
    print(key)