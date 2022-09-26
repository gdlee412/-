student1 = {'학번':2022001, '이름':'이순신', '학과':'불멸학과'}
print(student1)
print(student1['학번'], student1['이름'], student1['학과'])
print()
student1['연락처'] = '010-4061-6911'
print(student1)
print()
del student1['연락처']
print(student1)