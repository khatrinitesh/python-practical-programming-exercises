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
# for num in numbers:
#     total += num
# print(total)
# numbers = [1,2,3,4]
# total = 0 
# for num in numbers:
#     total += num 
# print(total)
# numbers = [1,2,3,4]
# total = 0
# for num in numbers:
#     total += num 
# print(total)
# Day 12 Lists (very important) > basic example manual sum
# numbers = [10,20,30,40,50]
# total = 0
# for num in numbers:
#     total += num 
# print(total)
# Day 12 Lists (very important) > using built in function 
# numbers = [10,20,30,40,50]
# total = sum(numbers)
# print(total0)
# Day 12 Lists (very important) > user input list 
# numbers = []
# n = int(input('how many numbers? '))
# for i in range(n):
#     num = int(input('enter number: '))
#     numbers.append(num)
# print("List:",i * numbers)
# print("List:",sum(numbers))
# numbers = []
# n = int(input('how many numbers: '))
# for i in range(n):
#     num = int('enter number: ')
#     numbers.append(num) 
# print('List:',numbers)
# print('Sum:',sum(numbers))
# Day 12 Lists (very important) > sum of even numbers only 
# numbers = [1,2,3,4,5,6]
# total = 0
# for num in numbers:
#     if num % 2 == 0:
#         total += num
# print('Even sum',total)
# Day 12 Lists (very important) > sum of odd numbers
# numbers = [1,2,3,4,5,6]
# total = 0
# for num in numbers:
#     if num % 2 != 0:
#         total += num 
# print('Odd sum',total)
# Day 12 Lists (very important) > challenge practice
# numbers = [10, 20, 30, 40]
# total = sum(numbers)
# print('sum',total)
# average = total / len(numbers)
# print(average)
# Day 12 Lists (very important) > bonus challenge important for interviews
# numbers = [10, 50, 20, 80, 30]
# largest = numbers[0]
# for num in numbers:
#     if num > largest:
#         largest = num 
# print("Largest:",largest)
# print('np max', np.max(numbers))
# print('np min', np.min(numbers))

# price = int(input('Enter price: '))
# discount = int(input('how many discount: '))
# final_price = price - price * discount / 100
# print(final_price)

# https://www.youtube.com/watch?v=iCwkuJOxvRI&list=PL3JNM3ENFH-5r3mRfuIbXLRCvtNK0FhmU
# Rent calculator in python | Mini Python Project with source code
# rent = int(input('enter your hostel/flat rent = '))
# food = int(input('enter the amount of food ordered = '))
# electricity_spend = int(input('enter the total of electricity spend = '))
# charge_per_unit = int(input('enter the charge per unit = '))
# persons = int(input('enter the number of persons living in room/flat = '))
# total_bill = electricity_spend * charge_per_unit
# print(total_bill)
# output = (food + rent + total_bill) // persons 
# print('each person will pay = ',output)

# Day 15 Tuples & Sets > 1. Basic Tuple Example
# numbers = (10, 20, 30, 40)
# print('Tuple',numbers)
# print('First element:',numbers[0])
# Day 15 Tuples & Sets > loop through tuple 
# numbers = (5, 10, 15, 20)
# for num in numbers:
#     print(num)
# Day 15 Tuples & Sets > count & index 
# numbers = (10, 20, 30, 20, 40)
# print('count of 20:',numbers.count(20))
# print('Index of 30:',numbers.index(30))
# Day 15 Tuples & Sets > tuple unpacking 
data = (100,200,300)
a,b,c = data 
print(a)
print(b)
print(c)
coordinates = (35,36,37)
a,b,c= coordinates
print(a)
print(b)
print(c)
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green,yellow,*red) = fruits 
print('green',{green})
print('yellow',{yellow})
print(f"Green: {green}")
print(f"Yellow: {yellow}")
print(f"Red: {red}")
happywords = ('smile','happy','sad','angry')
(a,b,*c) = happywords 
print(f"smile",{a})
print(f"happy",{b})
print(f"otherwise",{c})