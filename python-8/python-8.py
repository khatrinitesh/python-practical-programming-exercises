
# Day 01: Introduction
# # print('hello world')


# Day 02: Primitive Data Types
# name = 'nitesh' # string 
# age = 30 # int 
# salary = 5000.5 # float 
# isDev = True # boolean 
# print(type(name))
# print(type(age))
# print(type(salary))
# print(type(isDev))

# Day 03: Type Conversion
# age = '30'
# age = int(age)
# price = 100 
# price = float(price)
# print(type(price))

# Day 05: Operators
# a = 10 
# b = 5 
# print(a + b)
# print(a > b)

# Day 06: If Else
# age = 18 
# result = ''
# if age>=18:
#     result = 'adult'
# else:
#     result = 'minor'
# print(result)

# odd = 12
# even = 11
# if odd % 2 == 0:
#     print('even')
# elif odd % 2 != 0:
#     print('odd')

# Day 08: Loop
# for i in range(1,11):
#     print(i)

# Day 10: Functions
# def greet(name):
#     return f'hello {name}'
# print(greet('sameet'))

# DAY 12–16: Data Structures
# LIST
# nums = [1,2,3,4,5]
# nums.append(66)
# print(nums)
# TUPLE
# data = (1,2,3,4,5)
# print(data)
# SET 
# s = {1,2,3,4,5}
# print(s)
# # DICTIONARY
# user = {
#     "name": "nitesh",
#     "age": 30,
#     "salary": 5000.5
# }
# print(user['name'],'-',user['age'],'-',user['salary'])

# for i in range(1,20):
#     if(i == 5):
#         break
#     print(i)

# text = "hello"
# print(text.upper())

# class User:
#     def __init__(self, name):
#         self.name = name

# u = User("Nitesh")
# print(u.name)

# class Admin(User):
#     def role(self):
#         return "Admin"

# def add(a, b):
#     return a + b
# print(add(10,20))

# try:
#     x = int("abc")
# except:
#     print("Error")

# import math
# print(math.sqrt(16))

# import mysql.connector
# db =   mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="1234",
#     database="test"
# )


# import threading
# def task():
#     print('Running')
# t = threading.Thread(target=task)   
# t.start()

# import pandas as pd
# df = pd.read_csv("data.csv")
# print(df.head())

# import numpy as np

# arr = np.array([1,2,3])
# print(arr.mean())

# import matplotlib.pyplot as plt
# plt.plot([1,2,3],[4,5,6])
# plt.show()

# import re

# text = "my number is 9876543210"
# print(re.findall(r"\d+", text))

# square = lambda x: x * x
# print(square(5))

# def fact(n):
#     if n == 1:
#         return 1
#     return n * fact(n-1)

# import requests
# from bs4 import BeautifulSoup

# res = requests.get("https://example.com")

# import json

# data = {"name": "Nitesh"}
# print(json.dumps(data))

# from sklearn.linear_model import LinearRegression

# import json

# data = {"name": "Nitesh"}
# print(json.dumps(data))


