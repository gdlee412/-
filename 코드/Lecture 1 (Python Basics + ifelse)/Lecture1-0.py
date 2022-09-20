x = 5
print("x = ", x, type(x))
y = 3.14
print("y = ", y, type(y))
z = "Hello"
print(z, type(z))

#must make sure the input type is right sometimes
a = 100
b = 200
print(a + b)
a = '100'
b = '200'
print(a + b)

#inputs
name = input("Input Name: ")
age = int(input("Input Age: "))
print("Hi " + name + "! Nice to meet you. You are", age, "years old")

#if else
height = float(input())
weight = int(input())

BMI = weight / (height ** 2)

if BMI >= 35:
	print("고도비만")
elif BMI >= 30:
	print("중도비만")
elif BMI >= 25:
	print("경도비만")
elif BMI >= 23:
	print("과체중")
elif BMI >= 18.5:
	print("정상")
else:
	print("저체중")