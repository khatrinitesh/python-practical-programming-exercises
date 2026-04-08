
from collections import Counter

# day 1 basics (input + output) goal: take user input and print result 
# name = input('enter your name: ')
# age = input('enter your age: ')
# print('hello',name)
# print('you are',age,'years old')

# # day 2 conditions (if-else) goal:checker even/odd number 
# num = int(input('enter number: '))
# if num % 2 == 0:
#     print('even number')
# else:
#     print('odd number')

# day 3 loops for loop goal:print table
# num = int(input('enter number: '))
# for i in range(1,11):
#     print(num,'x','=',num * i)

# day 4 functions goal:create reusable function 
# def greet(name):
#     print('welcome',name)
# print('sameet')
# print('nitesh')
# print('pamisha')
# print('manisha')
# print('urvashi')
# print('arvind')

# day 5 lists goal:store multiple values
# fruits = ["apple", "banana", "mango"]
# for fruit in fruits:
#     print(fruit)
# fruits.append('grape')
# print(fruits)
# fruits.remove('apple')
# print(fruits)

# day 6 file handling = goal:write and read file 
# write file
# with open('data.txt','w') as file:
#     file.write('hello nitesh \n Learning Python')
# # read file 
# with open('data1.txt','r') as file:
#     print(file.read())

# day 7 mini project - goal:simple login system
# username = input('enter your username: ')
# password = input('enter your password: ')
# if username == 'admin' and password == '1234':
#     print('login successful')
# else:
#     print('Invalid credentials')

# day 1 log file analyzer > goal: count errors, warnings from a log file 
# with open('log.txt','r') as file:
#     lines = file.readlines()

# counter = counter()

# for line in lines:
#     if "ERROR" in line:
#         counter['ERROR'] += 1
#     elif 'WARNING' in line:
#         counter['WARNING'] += 1
#     elif 'INFO' in line:
#         counter['INFO'] += 1

# print(counter)

# Day 2: Password Strength Checker
# import re 
# password = input('enter password: ')
# if (len(password) >=8 and 
#     re.search('[A-Z]',password) and 
#     re.search('[a-z]',password) and
#     re.search('[0-9]',password) and 
#     re.search('[@%$]',password)):
#     print('strong password')
# else:
#     print('weak password')

# day 3: api data fetch (real-world) goal:fetch api and display data
# import requests
# api_json_placeholder = 'https://jsonplaceholder.typicode.com/posts'
# response = requests.get(api_json_placeholder)
# data = response.json()
# for post in data[:5]:
#     print(post['id'],'-',post['title'])

# for i in range(1,100):
#     response = requests.get(f"{api_json_placeholder}/{i}")
#     data = response.json() 
#     print(data['id'], "-",data['title'])
# for i in range(1,100):
#     response = requests.get(f"{api_json_placeholder}/{i}")
#     data = response.json()
#     print(data['id'],'-',data['title'],'-',data['body'])
# params = {
#     "id":[1,2,3,4,5]
# }
# response = requests.get(api_json_placeholder,params=params)
# data = response.json()
# for post in data:
#     print(post['id'],'-',post['title'])

# day 4 : cli to-do app persistant goal:store tasks in file
# def add_task(task):
#     with open("tasks.txt", "a") as file:
#         file.write(task + "\n")

# def view_tasks():
#     with open("tasks.txt", "r") as file:
#         print(file.read())

# while True:
#     choice = input("1.Add 2.View 3.Exit: ")

#     if choice == "1":
#         task = input("Enter task: ")
#         add_task(task)
#     elif choice == "2":
#         view_tasks()
#     else:
#         break

# def add_task(task):
#     with open('assignNew.txt','a') as file:
#         file.write(task + "\n")
# def view_task():
#     with open('assignNew.txt','r') as file:
#         print(file.read())
# while True:
#     choice = input('1.add 2.view 3.exit: ')
#     if choice == '1':
#         task = input('Enter task: ')
#         add_task(task)
#     elif choice == '2':
#         view_task()
#     else:
#         break

# # Write
# with open('demo.txt', 'w') as f:
#     f.write("First Line\nSecond Line\n")

# # Append
# with open('demo.txt', 'a') as f:
#     f.write("Third Line\n")

# # Read
# with open('demo.txt', 'r') as f:
#     for line in f:
#         print(line.strip())
# write
# with open('example.txt','w') as f:
#     f.write('first example \n')
# # append
# with open('example.txt','a') as f:
#     f.write('third example \n')
# # read
# with open('example.txt','r') as f: 
#     for line in f: 
#         print(line.strip())
# import csv

# with open("happy.csv", "r") as file:
#     reader = csv.DictReader(file)

#     for row in reader:
#         print(row["name"], row["age"])

# import os
# print(os.getcwd())


# with open('examplenew.txt','w') as f:
#     f.write('hello \n')

# with open('examplenew.txt','a') as f:
#     f.write('happy \n')

# with open('examplenew.txt','r') as f:
#     for line in f:
#         print(line.strip()) 

# import requests 
# api_json_placeholder = 'https://jsonplaceholder.typicode.com/posts'

# for i in range(1,100):
#     response = requests.get(f'{api_json_placeholder}/{i}')
#     data = response.json()
#     print(i,">",data['userId'],"-",data['title'])

# import os 
# import csv 
# if os.path.exists('happy.csv'):
#     with open('happy.csv') as f:
#         reader = csv.DictReader(f)
#         for row in reader:
#             print(row['name'],row['age'])
# else:
#     print('file not found. please create happy.csv')

# students = [
#     {"name": "Nitesh", "age": 30},
#     {"name": "Rahul", "age": 22},
#     {"name": "Amit", "age": 27}
# ]
# print('original students',students)
# students.append({"name":'test',"age":45})
# print('\nadded',students)
# students.insert(2,{"name":'test1',"age":65})
# print(students)
# new_students = [
#     {"name":'vijay',"age":40},
#     {"name":'chandresh',"age":42},
# ]
# print('new students',new_students)
# students_copy = students.copy()
# print('\nstudents copy',students_copy)

# colors = ["red", "green", "blue", "stop", "yellow"]

# for color in colors:
#     if color == "stop":
#         break
#     print(color)
    