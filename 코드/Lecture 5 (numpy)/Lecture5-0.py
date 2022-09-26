tuple1 = (1, 2, 3)
print(tuple1)
print()
#(1, 2, 3)
type(tuple1)
#<class 'tuple>

tuple2 = (2022001, '신사임당', (100, 90, 95))
print(tuple2)
#(2022001, '신사임당', (100, 90, 95))
print(tuple1[0], tuple1[1], tuple1[2])
#1, 2, 3
print(tuple2[0], tuple2[1], tuple2[2])
#2022001 신사임당 (100, 90, 95)

#tuple1[0] = 100
#error, cannot change tuple values