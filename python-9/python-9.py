
# day 1 - print and variables
# print('hello world')
# name = 'nitesh'
# age = 25 
# print('my name is', name, 'and i am', age, 'years old')
# practical example: user profile
# name = 'nitesh'
# city = 'mumbai'
# job = 'developer'
# print('name',name)
# print('city',city)
# print('job',job)
# concepts learned
# print()
# variables 
# strings 
# numbers

# day 2 - input from user 
# name = input('what is your name?')
# print('welcome',name)
# practical example:age calculator
# birth_year = int(input('what is your birth year'))
# current_year = 2026 
# age = current_year - birth_year 
# print('your age is',age)
# concepts learned 
# - input() 
# - int 
# - user interaction 

# day 3 - conditions (if, else)
# practical examples: voting eligibility 
# age = int(input('enter your age'))
# if age >= 18:
#     print('you are eligible to vote')
# else:   
#     print('you cannot vote')
# practical examples:even or odd 
# number = int(input('enter a number'))
# if number % 2 == 0:
#     print('the number is even')
# else:
#     print('the number is odd')
# concepts learned 
# - if 
# - else 
# - comparison operators 

# day 4 - loops for loop example 
# for i in range(1,5):
#     print('iteration',i)
# practical example: multiplication table 
# num = int(input('enter a number'))
# for i in range(1,11): 
#     print(num,'x',i,'=',num*i)
# while loop
# count = 1 
# while count <= 5: 
#     print('count is',count)
#     count += 1
# concepts learned
# - for 
# - while 
# - range()

# day 5 - functions 
# practical example: calculator function 
# def add(a,b): 
#     return a + b 
# result = add(10,20)
# print('the sum is',result)
# def add(a,b):
#     print(a+b) 
# result = add(10,20)
# practical example: greeting app 
# def greet(name):
#     print('hello',name)
# greet('nitesh')

# def greet(name):
#     print('hello',name)
# greet('nitesh')

# day 1 - print and variables 
# student information
# name = 'nitesh'
# age = 24 
# city = 'mumbai'
# print('name',name)
# print('age',age)
# print('city',city)
# practical task 
# create your own profile
# name = 'your name'
# email = 'your@email.com'
# phone = 1234567890
# print(name,'\n',email,'\n',phone,'\n')

# day 2 - input from user 
# goal - take user input 
# example: simple login
# name = input('what is your name?')
# print(name)

# practical task - ask age and city 
# age = int(input('what is your age?'))
# city = input('what is your city?')
# print('your age is',age)
# print('you live in',city)

# day 3 - numbers and calculator 
# goal : perform calculations 
# num1 = int(input('enter first number'))
# num2 = int(input('enter second number'))
# sum = num1 + num2
# print('the sum is',sum)

# project task : create mini calculator 
# a = int(input('enter first number'))
# b = int(input('enter second number'))
# print('addition',a+b)
# print('subtraction',a-b)
# print('multiply',a*b)
# print('divide',a/b)

# day 4 - if else (decision making)
# goal : learn conditions 
# vote eligibility
# age = int(input('enter your age'))
# if age >= 18:
#     print('you are eligible to vote')
# else:
#     print('you are not eligible to vote')
# practical task : check even or odd number 
# num = int(input('enter a number'))
# if num % 2 == 0:
#     print('the number is even')
# else:
#     print('the number is odd')

# day 5 - loops
# goal : repeat actions
# example: print numbers
# for i in range(1,6):
#     print(i)
# practical task: print multiplication table
# num = int(input('enter a number'))
# for i in range(1,11):
#     print(num,'x',i,'=',num*i)

# day 6 - lists
# goal : store multiple values
# example: student names 
# student = ['nitesh','suresh','ramesh']
# print(student)
# print(student[0])
# print(student[1])
# print(student[2])

# day 7 - mini project lists 
# name = input('enter students name: ')
# marks = int(input('enter marks: '))
# if marks >= 35:
#     result = 'pass'
# else:
#     result = 'fail'
# print('name',name)
# print('name',marks)
# print('name',result)
# daily practice formula
# every do this
# 1 Hour Plan

# 20 min → Learn concept
# 20 min → Type example code
# 20 min → Build small practical project

# Example:

# Variables → Student profile
# Input → Login form
# Conditions → ATM check
# Loops → Table generator
# List → Todo app
# Functions → Calculator
# File handling → Notes saver

# day 2 - input - login form 
# username = input('enter your username: ')
# print('welcome',username)
# type example code 
# email = input('enter your email: ')
# password = input('enter your password: ')
# print('email',email)
# print('password',password)
# build practical project 
# correct_username = 'admin'
# correct_password = 1234 
# username = input('enter username:')
# password = int(input('enter password:'))
# if username == correct_username and password == correct_password:
#     print('login successful')
# else:
#     print('invalid credentials')

# day 3 - conditions - ATM check 
# learn concept 
# if else checks conditions example you asked
# age = 20 
# if age >= 20:
#     print('you can vote')
# else:
#     print('you cannot vote')

# type example code 
# marks = 45
# if marks >= 35:
#     print('you passed')
# else:   
#     print('you failed') 

# build practical project 
# atm balance check 
# balance = 500 
# withdraw =  int(input('enter amount to withdraw:'))
# if withdraw <= balance:  
#     balance -= withdraw 
#     print('withdraw successful')
#     print('remaining balance',balance)
# else:
#     print('insufficient balance')

# day 4 - loops - table generator
# learn concept 
# loops repeat code 
# num = int(input('enter a number: '))
# for i in range(1,11):
#     print(num,'x',i,'=',num*i)
# for i in range(1,100):
#     if i % 3 == 0 and i % 5 == 0:
#         print('a')
#     elif i % 3 == 0:
#         print('b')
#     elif i % 5 == 0:
#         print('c')
#     else:
#         print(i)

# day 5 - list - to do app 
# learn concept 
# list stores multiple values 
fruits = ['apple','banana','orange']
print(fruits)
print(fruits[0])
print(fruits[1])
print(fruits[2])
# type example code 
# students = ['nitesh','suresh','ramesh']
# print(students)
# print(students[0])
# print(students[1])
# print(students[2])
# for student in students:
#     print(student)

# build practical project simple to do app 
# tasks = []
# tasks1 = input('enter a task: ')
# tasks2 = input('enter another task: ')
# tasks.append(tasks1)
# tasks.append(tasks2)
# for i,tasks in enumerate(tasks):
#     print(i+1,tasks)

# day 6 - functions calculator 
# learn concept function avoid repeating code 
# def greet(name):
#     print('hello',name  )

# type example code 
# def add(a,b):
#     print(a+b)
# add(10,20)

# build practical project - calculator 
# def add(a,b):
#     return a + b 
# num1 = int(input('enter first number: '))
# num2 = int(input('enter second number: '))
# result = add(num1, num2)
# print('the sum is:', result)

# calcaultor 
# def add(a,b):
#     return a + b 
# n1 = int(input('enter 1st number: '))
# n2 = int(input('enter 2nd number: '))
# result = add(n1,n2)
# print(result)

# day 7 handling notes saver learn concept file stores data permanently 
# note = input('write something')
# file = open('notes.txt','w')
# file.write(note)
# file.close()
# print('saved successfully')

# notes saver app - build practical project
# note = input('write something')
# file = open('notesapp.xls','w')
# file.write(note)
# file.close()



