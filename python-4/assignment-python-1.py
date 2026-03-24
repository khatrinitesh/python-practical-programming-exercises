import numpy as np

# basic variable practice
# name = 'test'
# age = 22
# height = 5.8
# is_student = True 
# print('basic variable practice',name)
# print('basic variable practice',age)
# print('basic variable practice',height)
# print('basic variable practice',is_student)

# check data types
# name = 'python'
# age = 32
# price = 99.99
# is_active = False
# print('Check data types',type(name))
# print('Check data types',type(age))
# print('Check data types',type(price))
# print('Check data types',type(is_active))

# SImple calculations
# a = 10
# b = 5
# print("Addition",a+b)
# print("Subtraction",a-b)
# print("Multiplication",a*b)
# print("Division",a/b)

# User input practice
# name = input('Enter your name: ')
# age = input('Enter your age: ')
# print(name)
# print(age)

# Type conversion
# x = '10'
# y = 5
# print(int(x) + y)

# boolean practice
# age = 20
# is_adult = age >= 18
# print(is_adult)

# Mini Exercise (must try)
# name = input('Enter name: ')
# age = input('Enter age: ')
# salary = input('Enter salary: ')
# print("Name:", name)
# print("Age:", age)
# print("Salary:", salary)

# Create Arrays 
# a = np.array([10,20,30])
# b = np.array([1,2,3])
# print(a)
# print(b)

# addition
# a = np.array([10,20,30])
# b = np.array([1,2,3])
# result = a + b 
# print("Addition",result)

# subtraction 
# a = np.array([10,20,30])
# b = np.array([1,2,3])
# result = a - b 
# print(result)

# multiplication
# a = np.array([10,20,30])
# b = np.array([1,2,3])
# result = a*b
# print(result)

# division 
# a = np.array([1044,2000,306])
# b = np.array([144,244,65])
# result = a / b 
# print(result)

# practice with user input 
# a = np.array(list(map(int,input('enter first array:').split())))
# b = np.array(list(map(int,input('enter second array:').split())))
# print("Add:",a+b)
# print("Sub:",a-b)
# print("Mul:",a*b)
# print("Div:",a/b)

# mini exercise (must try)
# arr = np.array([5,10,15,20,25])
# print('sum',np.sum(arr))
# print('average',np.mean(arr))
# print('maximum',np.max(arr))

# Day 4 >  arithmetic operators 
# a = 10 
# b = 3
# print("Addition",a+b)
# print("Subtraction",a-b)
# print("Multiply",a*b)
# print("Division",a/b)
# print("Modulus (remainder)",a%b)

# Day 4 > Comparison operators (==,>,<)
# x = 5 
# y = 10
# print('Equal',x==y)
# print('greater',x>y)
# print('less',x<y)

# Day 4 > User input + operators
# num1 = int(input('enter first number:'))
# num2 = int(input('enter second number:'))
# print("sum:",num1 + num2)
# print("is first number greater:",num1 > num2)

# Day 4 > even or odd (using %)
# num = int(input('enter a number:'))
# if num % 2 == 0:
#     print('even number')
# else:
#     print('odd number')

# Day 4 > compare two numbers
# a = int(input('enter pawan 1: '))
# b = int(input('enter nitesh 2: '))
# if a > b :
#     print('pawan is greater')
# elif a < b :
#     print('nitesh is greater')
# else:
#     print('both are equal')

#  Day 4 > real-life example (discount calculation)
# price = float(input("Enter price: "))
# discount = float(input("Enter percentage: "))
# final_price = price - (price * discount / 100)
# print("Final price",final_price)

# Day 4 > Mini Challenge 
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# c = int(input("Enter third number: "))
# print("Add", a + b)
# print("Sub", a - b)
# print("Mul", a * b)
# print("Div", a / b)

# Day 5 > Basic If-Else
# age = 18
# if age >= 18:
#     print('you are an adult')
# else:
#     print('you are a minor')

# Day 5 > User input condition 
# age = int(input("enter your age: "))
# if age > 20:
#     print("you can vote")
# else:
#     print("you cannot vote")

# Day 5 > even or odd 
# num = int(input('enter a number: '))
# if num % 2 == 0:
#     print('Yes, it is even number')
# else:
#     print('No, it is even number')

# Day 5 > Positive, Negative or Zero 
# num = int(input('Enter a number: '))
# if num > 0:
#     print('positive')
# elif num < 0:
#     print('negative')
# else:
#     print('zero')

# num = int(input('Enter your age: '))
# if num >= 35:
#     print('A is excellent')
# elif num >= 45:
#     print('b is average')
# else:
#     print('c is failed')

# Day 5 >Find largest of two numbers
# a = int(input('Enter first number: '))
# b = int(input('Enter second number: '))
# if a > b :
#     print("A is greater")
# elif a > b:
#     print("B is less")
# else:
#     print("Failed")

# Day 5 > find largest of three numbers
# a = int(input('Enter first number: '))
# b = int(input('Enter second number: '))
# c = int(input('Enter third number: '))
# if  a > b and a > c:
#     print('A is largest')
# elif b > c:
#     print('B is largest')
# else:
#     print("C is largest")

# Day 5 Grade calculator 
# marks = int(input('Enter your marks: '))
# if marks >= 90:
#     print('Grade A')
# elif marks >= 50:
#     print('Grade B')
# elif marks >= 35:
#         print('Grade C')
# else:
#     print('Fail')

# Day 5 simple login system
# username = input('enter username: ')
# password = input('enter password: ')
# if username == 'pawan' and password == 'pawan@1234':
#     print('Login successful')
# else:
#         print('invalid credentials')

# Day 5 Real life example
# temperature = int(input('enter temperature: '))
# if temperature > 30:
#     print('it is hot')
# elif temperature > 20:
#     print('nice weather')
# else:
#     print('it is cold')

# Day 6 Nested conditions + Practice > Basic example
# age = 20
# has_id = True
# if age >= 18:
#     if has_id:
#         print(" you can enter")
#     else:
#         print("ID required")
# else:
#     print("You are underage")

# Day 6 Nested conditions + Practice > student grade system
# marks = 85
# if marks >= 50:
#     if marks >= 90:
#         print("Grade A")
#     elif marks >= 75:
#         print("Grade B")
#     else:
#         print("Grade C")
# else:
#     print("Failed")

# Day 6 Nested conditions + Practice > Salary bonus example
# salary = 40000
# years = 3
# if salary > 30000:
#     if years >= 2:
#         print('Bonus eligible')
#     else:
#         print('Work more years')
# else:
#     print('Salary too low')

# Day 6 Nested conditions + Practice > login system
# username = 'admin'
# password = '1234'
# u = input('enter username: ')
# p = input('enter password: ')
# if u == username:
#     if p == password:
#         print('Login successful')
#     else:
#         print('Wrong password')
# else:
#     print('User not found')

# Day 6 Nested conditions + Practice > traffic signal example
# color = 'red'
# if color == 'red':
#     print('Stop')
# elif color == 'yellow':
#     print('Ready')
# else:
#     if color == 'green':
#         print('Go')
#     else:
#         print("invalid signal")
    