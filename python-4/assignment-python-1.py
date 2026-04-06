import numpy as np
from collections import  Counter

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
    

# Day 7 Mini Example 1 : Even / odd number
# num = int(input('enter a number:'))
# if num % 2 == 0:
#     print('even number')
# else:
#     print('odd number')

# Day 7 Mini Example 2 : Simple calculator
# num1 = float(input('enter first number'))
# num2 = float(input('enter second number'))
# operation = input('choose operation (+,-,,*,/):')
# if operation == '+':
#     print('Result',num1 + num2)
# elif operation == '-':
#     print('Result',num1 - num2)
# elif operation == '*':
#     print('Result',num1 * num2)
# elif operation == '/':
#     if operation != 0:
#         print('Result',num1 / num2)
#     else:
#         print('Cannot divide by zero')
# else:
#     print('Invalid operation')


# Day 7 🚀 Final Mini Project (Combine Both)
# print('1. Even/Odd checker')
# print('2. Simple calculator')
# choice = input('Choose option (1 or 2)')
# if choice == '1':
#     num = int(input('Enter a number: '))
#     if num % 2 == 0:
#         print('even number')
#     else:
#         print('odd number')
# elif choice == '2':
#     num1 = float(input('enter first number: '))
#     num2 = float(input('enter second number: '))
#     operation = input('Choose operation (+,-,*,/): ')
#     if operation == "+":
#         print('Result:',num1 + num2)
#     elif operation == '-':
#         print('Result:',num1 - num2)
#     elif operation == '*':
#         if num2 != 0:
#             print('Result',num1 / num2)
#         else:
#             print('Cannot divide by zero')
#     else:
#         print('Invalid operation')
# else:
#     print("invalid choice")

# Day 8 Loops (for loop) > 1 Basic for loop print numbers
# for i in range(1,20):
#     print(i)
# Day 8 Loops (for loop) > 2 even numbers using loop
# for i in range(1,20):
#     if i % 2 == 0:
#         print('even number: ',i)
#     if i % 2 != 0:
#         print('odd number: ',i)
# Day 8 Loops (for loop) > sum of numbers
# n = int(input('enter a number: '))
# total = 1
# for i in range(1,n+1):
#     total += i; 
#     print('Sum',total)
# for i in range(1,n+1):
#     total *= i
#     print('Multiple',total)
# for i in range(1,n+1):
#     total -= i 
#     print('Subtraction',total)


# Day 8 Loops (for loop) > 3 sum of numbers
# n = int(input('enter a number: '))
# total = 0
# for i in range(1,n+1):
#     total += i
# print('Sum:',total)

# Day 8 Loops (for loop) > 4 multiplication table 
# num = int(input('Enter a number: '))
# for i in range(1,11):
#     print(num,'x',i,num*i)
# Day 8 Loops (for loop) > 5 reverse loop
# for i in range(20,0,-1):
#     print(i)
# Day 8 Loops (for loop) > 6 string loop
# name = 'python'
# for ch in name:
#     print(ch)
# name = 'nitesh khatri'
# for i in range(len(name)):
#     print(i,name[i])
# for char in name:
#         print(char)
# Day 8 Loops (for loop) > mini project 
# rows = 5 
# for i in range(1,rows + 1):
#     print("*" * i)
# Day 8 Loops (for loop) >
# Day 9 While loop - 1 basic loop
# i = 1
# while i < 5:
#     print(i)
#     i += 1
# Day 9 while loop - 2 sum using while loop 
# n = int(input('enter a number: '))
# i = 1
# total = 0 
# while i <= n:
#     total += i 
#     i += 1 
# print("Sum:", total)
# Day 9 while loop - 3 even numbers
# n = int(input('enter number: '))
# i = 1
# while i <= n: 
#     if i % 2 == 0: 
#         print(i)
#     i += 1
# Day 9 while loop - 4 infinite loop (important concept)
# while True:
#     print('Hello')
# Day 9 while loop - 5 user input until exit 
# u = 'admin'
# p = 'admin@1234'
# if u == 'admin' and p == 'admin@1234':
#     print('login successfullly')
# else:
#     print('user not found')
# while True:
#     text = input('enter something (type "exit" to stop)')
#     if text == 'exit':
#         print("Program ended")
#         break
# Day 9 while loop - 6 password checker 
# correct_pwd =  '1234'
# while True:
#     password = input('Enter password: ')
#     if password == correct_pwd:
#         print('Access Granted')
#         break 
#     else:
#         print('Wrong password, try again')
# correct_pwd = '1234'
# while True:
#     password = input('Enter password: ')
#     if password == correct_pwd:
#         print('Access granted')
#         break 
#     else:
#         print('Wrong password, try again')

# Day 9 while loop - 7  guess the number game 
# secret = 7 
# while True:
#     guess = int(input("Guess number (1-10): "))
#     if guess > secret:
#         print('you win')
#         break
#     else:
#         print('try again')
# while True:
#     guess = int(input("Guess number (1-10): "))
#     if guess == secret:
#         print('you win')
#         break
#     else:
#         print('try again')
# while True:
#     guess = int(input("Guess number (1-10): "))
#     if guess != secret:
#         print('you win')
#         break
#     else:
#         print('try again')

# Day 10 Break continue - 1 break example (stop loop early)
# for i in range(1,11):
#     if i == 5: 
#         break
#     print(i)
# Day 10 Break continue -  2 Continue Example (Skip One Iteration)
# for i in range(1,11):
#     if i == 5:
#         continue
#     print(i)
# Day 10 Break continue - 3 break with while loop
# while True: 
#     num = int(input('Enter number (0 to stop): '))
#     if num == 0:
#         break
#     print('You entered:',num)
# Day 10 Break continue - 4 continue with while loop
# i = 0
# while i < 20: 
#     i += 1
#     if i < 8:
#         continue
#     print(i)
# i = 0 
# while i < 30:
#     i += 1
#     if i < 0:
#         continue
#     print(i)

# Day 10 Break continue - find first even number 
# numbers = [1, 3, 7, 9, 10, 13,14,16]
# for i in numbers: 
#     if i % 2 == 0:
#         print('first even:',i)
#         break
#     if i % 2 != 0:
#         print('first odd:',i)
#         break
# Day 10 Break continue - skip multiples of 3 
# for i in range(1,5):
#     if i % 3 == 0:
#         continue
#     print(i)
# Day 10 Break continue - mini project simple login system
# correct_pwd = '1234'
# attempts = 3 
# while attempts > 0:
#     password = input('enter password: ')
#     if password == correct_pwd:
#         print('login successful')
#         break 
#     else:
#         attempts -= 1
#         print('wrong password. attempts left:',attempts)
# if attempts == 0:
#     print('account locked')
# Day 11 Functions (def,num) > 1 basic function 
# def greet():
#     print('hello, welcome to python')
# greet()
# def example():
#     print('hello nitesh')
# example()
# Day 11 Functions (def,num) > function with parameters 
# def example(name):
#     print('hello',name)
# example('nitesh')
# def sum(a,b):
#     print('calculator',a+b)
# sum(10,20)
# Day 11 Functions (def,num) > function with return value 
# def add(a,b):
#     return a + b 
# result = add(10,40)
# print(result)
# def multiple(a,b):
#     return a * b 
# result = multiple(10,20)
# print(result)
# Day 11 Functions (def,num) > even/odd function
# def check_even_odd(num):
#     if num % 2 == 0:
#         return 'even'
#     else:
#         return 'odd'
# print(check_even_odd(10))
# print(check_even_odd(15))
# print(check_even_odd(23))
# def check_even_odd(num):
#     if num % 2 == 0:
#         return "even number"
#     else:
#         return "odd number"
# print(check_even_odd(20))
# print(check_even_odd(21))
# print(check_even_odd(22))
# print(check_even_odd(23))
# Day 11 Functions (def,num) > find maximum number
# def example(a,b):
#     if a > b:
#         return a 
#     else:
#         return b 
# print(example(10,20))
# arr = np.array([10,20])
# print(np.max(arr))
# print(np.min(arr))

# def example(a,b):
#     arr = np.array([a,b])
#     return np.max(arr)
# print(example(10,20))
# def example2(a,b,c):
#     arr = np.array([a,b,c])
#     return  np.max(arr)
# print(example2(30,40,50))
# def example3(a,b,c):
#     arr = np.array([a,b,c])
#     return  np.min(arr)
# print(example3(30,40,50))
# a = np.array([10,30,50])
# b = np.array([20,25,60])
# result = np.maximum(a,b)
# print(result)
# Day 11 Functions (def,num) > mini project calculator using functions
# def add(a,b):
#     return a+b 
# def subtract(a,b):
#     return a-b 
# def multiple(a,b):
#     return a*b 
# def divide(a,b):
#     if b!=0:
#         return a/b
#     else:
#         return "cannot divide by zero"
# while True:
#     print("\n1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5. Exit")

#     choice = input("Enter choice: ")

#     if choice == '5':
#         break 

#     num1 = float(input("Enter first number: "))
#     num2 = float(input("Enter second number: "))

#     if choice == '1':
#         print('Result',add(num1,num2))
#     elif choice == '2':
#         print('Result',subtract(num1,num2))
#     elif choice == '3':
#         print('Result',multiple(num1,num2))
#     elif choice =="4":
#         print('Result',divide(num1,num2))
#     else:
#         print('Invalid choice')

# Day 12 Lists (very important) > create a list 
# numbers = [1,2,3,4]
# print(numbers)
# Day 12 Lists (very important) > access list elements
# fruits = ['apple','watermelon','mango']
# print(fruits[0])
# print(fruits[1])
# Day 12 Lists (very important) > add items to list
# fruits = ['apple','banana']
# fruits.append('mango')
# fruits.append('grape')
# print(fruits)
# Day 12 Lists (very important) > remove items 
# fruits = ['apple','watermelon','mango']
# fruits.remove('watermelon')     # remove value
# fruits.pop() # remove last item 
# print(fruits)
# Day 12 Lists (very important) > loop through list 
# numbers = [10,20,30,40]
# for num in numbers:
#     print(num)
# Day 12 Lists (very important) > sum of list 
# numbers = [1,2,3,4]
# total = 0

# person = {
#     "name": "Alice",
#     "age": 25,
#     "city": "New York"
# }
# print(person)
# print(person["name"])

# fruitwise = ['apple','mango','grape','watermelon']
# [a,b,*c] = fruitwise
# print(f"a",a)
# print(f"b",b)
# print(f"c",c)

#Day 16 Dictionaries (key-value data 🔥) > 1 creating a dictionary 
# person = {
#     'name':'test',
#     'age':25,
#     'city':'india'
# }
# print(person)
# print(person['name'])


#Day 16 Dictionaries (key-value data 🔥) > 2 adding and updating key-value pairs 
# person['email']= 'xyz@gmail.com'
# person['age'] = 26
# person['mobileNum'] = 9145689745
# print(person)
#Day 16 Dictionaries (key-value data 🔥) > 3 removing items 
# person.pop('city') #removes city 
# print(person)
# last_item = person.popitem()
# print('removed:',last_item)
#Day 16 Dictionaries (key-value data 🔥) > 4 iterating over a dictionary 
# person = {
#     "name": "Alice",
#     "age": 25,
#     "city": "New York"
# }

# for key in person:
#     print(key,"->",person[key])
# for key,value in person.items():
#     print(f"{key} => {value}")
#Day 16 Dictionaries (key-value data 🔥) > 5 check if key exists
# if "name" in person: 
#     print('Name exists',person["name"])
# else:
#     print('name not found')
#Day 16 Dictionaries (key-value data 🔥) > 6 nested dictionaries (advanced)
# students = {
#     "101":{"name":"nitesh","score":90},
#     "102":{"name":"sameet","score":91},
# }
# print(students['102']['score'])
# print(students['102']['name'])
# students['103'] = {'name':'charlie','score':92}
# students['110'] = [{'name':'charlie1','score':85},{'name':'charlie1','score':87}]
# print(students) 
#Day 16 Dictionaries (key-value data 🔥) > 7 dictionary comprehension power 
# numbers = [1,2,3,4,5]
# squares = {n:n**2 for n in numbers}
# print(squares)
#Day 16 Dictionaries (key-value data 🔥) > 8 practice exercise your turn 
# products = [
#     ("Laptop", 1200),
#     ("Mouse", 25),
#     ("Keyboard", 75),
#     ("Monitor", 300)
# ]
# print(products)
# Day 17 string operations > 1 creating strings 
# name = 'tests'
# greeting = 'hello'
# print(name,greeting)
# Day 17 String operations > access characters & slicing
# text = 'python'
# print(text[0])
# print(text[1])
# print(text[0:4]) # start:end slice
# print(text[-1])
# print(text[::2]) #pto (every 2nd character) slice
# Day 17 String operations > string length
# msg = 'hello how are you'
# print(len(msg))
# Day 17 String operations > 1. convert to uppercase/lower/capitalize/title
# text = 'hello world'
# print(text.upper())
# print(text.lower())
# print(text.capitalize())
# print(text.title())
# text2 = 'PyThOn'
# print(text2.swapcase()) # swapcase
# text3 = 'aLIce'
# print('upper',text3.upper())


# Python Roadmap (Beginner → Intermediate)
# 1. Basics (Foundation) - Variables & Data types (int, float, str, bool)
# age = 20 
# year = 2026
# print(age)
# print(year + 5)
# price = 99.99
# discount = 10.5
# final_price = price - discount 
# print(final_price)
# name = 'rahul'
# city = 'mumbai'
# print('my name is ',name)
# print('my city is ',city)
# is_student = True 
# has_job = False
# print(is_student)
# print(has_job)
# is_raining = True
# if is_raining:
#     print('take an umbrella')
# name = 'text'
# age = 21 
# height = 5.7 
# is_graduated = False 
# print(name)
# print(age)
# print(height)
# print(is_graduated)
# 1. Basics (Foundation) - input/output 
# name = input('enter your name')
# print(name)
# color = input('what is your favorite color')
# print(color)
# 1. Basics (Foundation) - input with integer
# age = int(input('enter your age:'))
# print('next year you will be ',age + 1)
# 1. Basics (Foundation) - input with float
# price = float(input('Enter price: '))
# tax = float(input('enter tax: '))
# total = price + tax 
# print('total price',total)
# 1. Basics (Foundation) - multiple inputs 
# values = input("Enter two numbers: ").split()
# if len(values) != 2:
#     print('please enter exactly two numbers separated by space.')
# else:
#     a,b= map(int,values)
#     print('Sum',a+b)
# 1. Basics (Foundation) - output formatting
# name = 'rahul'
# marks = 85
# # print('my name ',name,'and i scored',marks)
# print(f'my name is',name,'and i scored ',marks)
# 1. Basics (Foundation) - operators - addition
# a = 10
# b = 10
# print(a+b)

# 1. Basics (Foundation) - operators - subtraction
# x = 180
# y = 150
# print(x-y)

# 1. Basics (Foundation) - operators - multiplication 
# xx= 200
# yy = 220
# print(xx*yy)

# 1. Basics (Foundation) - operators - division
# a = 100
# b = 5
# print(a/b)

# 1. Basics (Foundation) - operators - mixed operations
# a=10
# b=5
# c=2
# result = a+b*c 
# print(result)

# 1. Basics (Foundation) - operators - using input + operators
# a = int(input('enter first number: '))
# b = int(input('enter second number: '))
# print("sum:",a+b)
# print("difference:",a-b)

# 1. Basics (Foundation) - Conditionals (if, elif, else) - basic if
# age = 18 
# if(age >= 18):
#     print('you can vote')
# 1. Basics (Foundation) - Conditionals (if, elif, else) - if-else
# num = 7
# if num % 2 == 0:
#     print('even number')
# else:
#     print('odd number')
# # 1. Basics (Foundation) - Conditionals (if, elif, else) - if-elif-else
# marks = 25
# if marks >= 90:
#     print('Grade A')
# elif marks >= 75:
#     print('Grade B')
# elif marks >= 35:
#     print('Grade C')
# else:
#     print('Failed')
# # 1. Basics (Foundation) - Conditionals (if, elif, else) - using input 
# age = int(input('enter your age: '))
# if age >= 18:
#     print('Adult')
# else:
#     print('Minor')
# # 1. Basics (Foundation) - Conditionals (if, elif, else) - multiple conditions
# num = 0
# if num >  0 and num % 2== 0:
#     print('Positive even number')
# elif num % 2 != 0:
#     print('Positive odd number')
# else:
#     print('negative')
# # 1. Basics (Foundation) - Conditionals (if, elif, else) - nested if 
# age = 20
# has_id = True 
# if age >= 18:
#     if has_id:
#         print('allowed entry')
#     else:
#         print('ID required')
# else:
#     print('Not allowed')
# # 1. Basics (Foundation) - Loops (for, while) > 1. for Loop – Iterating over numbers
# for i in range(1,6):
#     print(i)
# # 1. Basics (Foundation) - Loops (for, while) > 2. for Loop – Iterating over a list
# fruits = ["apple", "banana", "cherry"]
# for i in fruits:
#     print(i)
# # 1. Basics (Foundation) - Loops (for, while) > 3 while loop - basic
# i = 0 
# while i <= 10:
#     i+= 1
#     print(i)
# # 1. Basics (Foundation) - Loops (for, while) > 4. while loop with condition
# n = int(input('enter a number'))
# i = 1 
# while i <= n:
#     print(i * i)
#     i += 1
# # 1. Basics (Foundation) - Loops (for, while) > 5. nested loop
# Print a 3x3 square of stars
# for i in range(3):
#     for j in range(3):
#         print("*",end=" ")
#         print()
# # 1. Basics (Foundation) - Loops (for, while) > 6. using break & continue 
# for i in range(1,11):
#     if i == 6:
#         break 
#     print(i)

# for i in range(1,20):
#     if i == 5:
#         continue
#     print(i)
# 2. Data Structures > 1. Creating a List
# numbers = [10,20,30,40,50]
# print(numbers)
# fruitwise = ['apple','watermelon','pineapple','mango','guava']
# print(fruitwise)
# 2. Data Structures > 2. accessing elements
# fruits = ['apple','banana','cherry']
# print(fruits[0]) # firsts item
# print(fruits[-1]) # last item
# 2. Data Structures > adding items
# numbers = [1,2,3]
# numbers.append(4)
# print(numbers) # add at the end
# numbers.insert(1,5) # add 5 at index 1 
# print(numbers)
# 2. Data Structures > 4. removing items 
# numbers = [1,2,3,4,5]
# numbers.remove(3)
# print('Removed',numbers)
# numbers.pop()
# print('Pop',numbers) # remove last item
# 2. Data Structures > 5. looping though a list 
# fruits = ['apple','watermelon','cherry']
# for fruit in fruits:
#     print(fruit)
# 2. Data Structures > 6. list operations 
# a = [1,2,3]
# b = [4,5,6]
# concatenate list
# c = a + b 
# print(c)
# repeat list 
# d = a * 2 
# print(d)
# 2. Data Structures > 7. list slicing 
# numbers = [10,20,30,40,50]
# print(numbers[1:4]) # items at index 1,2,3
# print(numbers[:3]) # first 3 items
# print(numbers[::2]) # every 2nd item
# 2. Data Structures > 1. creating a tuple
# numbers = (10,20,30,40,50)
# print(numbers)
# 2. Data Structures > 2. accessing elements
# numbers = ('apple','mango','watermelon','banana')
# print(numbers[0]) # first item
# print(numbers[-1]) #last item
# 2. Data Structures > 3. tuple slicing 
# numbers = (10,20,30,40,50)
# print(numbers[1:4]) # 20,30,40
# print(numbers[:3]) # first 3 items
# print(numbers[::2])
# 2. Data Structures > 4. tuple is immutable 
# numbers = (1, 2, 3)
# print(numbers[0] = 10)
# 2. Data Structures > 5. looping through tuple
# colors = ('red','green','blue')
# print(colors)
# print(f"colors: ",colors)
# for color in colors:
#     print(f'color: ',color) # each item in tuple
# 2. Data Structures > 6. tuple operations
# a = (1,2,3)
# b = (4,5)
# print(a + b) # combine tuples
# print((a+b)*2) # repeat tuple
# 2. Data Structures > 7. tuple methods
# numbers = (1,2,2,3,4,5)
# unique_num = tuple(set(numbers))
# print(unique_num)
# fruitwise = ('apple','apple','mango')
# unique_fruitWise = tuple(set(fruitwise))
# print(unique_fruitWise)
# print(numbers.count(1)) #count occurrences
# print(numbers.index(3)) # find position
# 2. Data Structures > 8. packing and unpacking
# person =   ('Rahul',20,'Mumbai')
# name,age,city = person 
# print(name)
# print(age)
# print(city)
# print(f'name:',name,'age:',age,'city:',city)
# for i in person:
#     print(">",i,i)
# print(f'hello world -- ')
# x = 10
# y = 20
# print(x*y/100)
# price = float(input('enter a number:'))
# discount = float(input('enter a discount: '))
# finalCalc = price - (price * discount / 100) 
# print(finalCalc)

# day 18 - File Handling (read/write files) - 1 create and write to a file 
# with open('assignment.txt','w') as file:
#     file.write('hi how are you doing?\nNostrud excepteur proident eu mollit reprehenderit occaecat consequat nostrud dolore.\nAmet ullamco excepteur excepteur sunt id..')

# day 18 - File Handling (read/write files) - 2. Read a File
# with open('assignmenttwo.txt','r') as file:
#     for line in file:
#         print(line)

# day 18 - File Handling (read/write files) - 3. Append to a File
# with open('assignmentwo','a') as file:
#     file.write('your new line\n')

# day 18 - File Handling (read/write files) - 4 count lines in a file 
# with open('example.txt','r') as file:
#     lines = file.readlines()
#     print(lines)

# day 18 - File Handling (read/write files) - 5 read file as list 
# with open('example.txt','r') as file:
#     lines = file.readlines()
#     print(lines[1].strip())

# with open('example.txt','w') as file:
#     file.write('hi')

# with open('example.txt','a') as file:
#     file.write('hi how are you sam?')
# day 18 - File Handling (read/write files) - 7 count words in a file
# with open('wordExcel.txt','r') as file:
#     text = file.read()
#     words = text.split()
#     print(len(words))
# day 18 - File Handling (read/write files) - find a word in a file
# with open('assignmentwords.txt','r') as file:
#     text = file.read()
#     if 'python' in text:
#         print('found')
#     else:
#         print('not found')
# day 18 - File Handling (read/write files) - 9. remove a file
# import os
# if os.path.exists('copy.txt'):
#     os.remove('copy.txt')

# day 18 - File Handling (read/write files) - advanced count frequency of each word

# with open('wonderful.txt','w') as file:
#     file.write('python is a programming coding. 123')
    
# with open('wonderful.txt','r') as file:
#     words = file.read().split()
#     print(Counter(words))