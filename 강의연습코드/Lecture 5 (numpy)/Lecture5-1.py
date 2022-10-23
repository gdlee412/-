set1 = set([3, 2, 1, 2, 3])
print(set1)
#{1, 2, 3}
type(set1)
#<class 'set'>
set2 = set("Hello")
print(set2)
#{'o', 'H', 'e', 'l'}
#can change

#print(set1[0])
#error, sets dont have indices

#we can change to list anf print list
lst1 = list(set1)
print(lst1)
#[1, 2, 3]
print(lst1[0])
#1