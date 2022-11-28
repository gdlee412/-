fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']

print(fruits)
print(fruits.count('apple'))
print(fruits.index('pear'))

fruits.reverse()
print("After reverse: ")
print(fruits)

fruits.append('grape')
print("After append: ")
print(fruits)

fruits.insert(1, 'grape')
print("After insert: ")
print(fruits)

fruits.sort()
print("After sort: ")
print(fruits)

fruits.pop()
print("After pop: ")
print(fruits)

fruits.remove('banana')
print("After remove: ")
print(fruits)