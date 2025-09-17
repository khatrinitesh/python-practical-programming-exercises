# # Python Built in Functions
# def example1():
#     number1 = -10
#     absNum = abs(number1)
#     return absNum
# result1 = example1()
# print('Result 1',result1)

# def example2():
#     number2 = 7 
#     absNum = abs(number2) 
#     return absNum
# result2 = example2()
# print('Result 2',result2)

# def example3():
#     number3 = -3.5
#     absNum = abs(number3)
#     return absNum
# result3 = example3()
# print('Result 3',result3)

# def example4():
#     values = [True, 1, "text", [1], 10]
#     allValues = all(values)
#     return allValues
# result4 = example4()
# print('Result 4:',result4)

# def example5():
#     values = [True, 1, 0, "text"]
#     return values
# result5 = example5()
# print('Result 5:',result5)

# def example6():
#     numbers = [2, 4, 6, 8]
#     all_even = all(n % 2 == 0 for n in numbers)
#     return all_even
# result6 = example6()
# print('Result 6:',result6)

# def example7():
#     print(all([]))
# result7 = example7()
# print('Result 7:',result7)

# def example8():
#     values = [False,0,"",5]
#     return values
# result8 = example8()
# print('Result 8:',result8)

# def example9():
#     values = [False, 0, "", None]
#     return values
# result9 = example9()
# print('Result 9:',result9)

# def example10():
#     numbers = [1, 3, 5, 6]
#     has_even = any(n % 2 == 0 for n in numbers)
#     return has_even
# result10 = example10()
# print('Result 10:',result10)

# def example11():
#     result = bool(1)
#     return result 
# result11 = example11()
# print('Result 11:',result11)

# def example12():
#     result = bool('nitesh')
#     return result 
# result12 = example12()
# print('Resutl12:', result12)

# def example13():
#     result = bool([1,2,3])
#     return result 
# result13 = example13()
# print('Result 13:',result13)

# def example14():
#     result = bool(0)
#     return result 
# result14 = example14()
# print('Result14:',result14)

# def example14():
#     result = bool("")
#     return result 
# result15 = example14()
# print('Result14:',result15)

# def example15():
#     result = bool([])
#     return result 
# result15 = example15()
# print('Result15:',result15)

# def example16():
#     result = bool(None)
#     return result 
# result16 = example16()
# print('Result 16:',result16)

# def example17():
#     expression = '3+5*2'
#     result = eval(expression)
#     return result
# result17 = example17()
# print('Result17:',result17)

# def example18():
#     x = 10 
#     y = 5 
#     return x + y 
# result18 = example18()
# print("Result18:",result18)

# def example19(n):
#     return n % 2 == 0
# numbers = [1, 2, 3, 4, 5, 6]
# result = filter(example19,numbers)
# print(list(result))

# def example20():
#     x = 10 
#     return x 
# print('Result20:',float(10))

# def example21():
#     x = "7"
#     return x 
# print('Result 21:',float(10))

# def example22():
#     x = 10 
#     return x/2
# print('Result 22:',float(10/2))

# def example23():
#     firstname = 'nitesh'
#     lastname = 'khatri'
#     return firstname + " " + lastname 
# fullname = example23()
# print(fullname)

# def example24(x, y): 
#     return x *y + 10 
# calculator = example24(30, 50)
# print(calculator)

# def example25(a,b):
#     return a * b 
# calculator = example25(20,30)
# print(calculator)

# def example26():
#     name = 'nitesh'
#     age = 30
#     return 'My name is {} and my age is {}.'.format(name, age)
# formatted_string = example26()
# print(formatted_string)

# def example27():
#     number = 255
#     return hex(number)
# result27=example27()
# print(result27)

# def example28():
#     return hex(10)
# result28=example28()
# print(result27)

# def example29():
#     a = 10 
#     b = 20
#     print("ID of a inside function:",id(a))
#     return a + b 
# example29()

# def example30():
#     a = 10
#     b = 20
#     return a 
# print(example30())

# # def example31():
# #     name = input('enter your name:')
# #     return name
# # result31 = example31()
# # print('hello',result31)

# def example32():
#     num = 5.8 
#     return num 
# result32 = example32()
# print(result32)

# def example33():
#     s = "123"
#     return s 
# result33 = example33()
# print("result33:",result33)

# def example34():
#     my_list = [1, 2, 3]
#     my_iterator = iter(my_list)
# result34 = example34()
# print(result34)

# def example35():
#     name = 'nitesh35'
#     return len(name)
# result35 = example35()
# print(result35)

# def example36():
#     fruits = ["apple", "banana", "cherry"]
#     return fruits
# result36 = example36()
# print(len(result36))

# def example37():
#     person = {"name": "Alice", "age": 30}
#     return person
# result37 = example37()
# print(len(result37))

# students_count = 1000
# print(students_count)
# rating=4>99
# print(rating)
# is_published = False 
# print(is_published)
# course_name = 'python programming'
# print(course_name)

# fruitswise = ['apple','pineapple','watermelon','guava']
# fruitswiseResult = len(fruitswise)
# print(fruitswise)


# def square(n):
#     return n * n 
# numbers = [1,2,3,4,5]
# squared = map(square,numbers)
# print(list(squared))

# numbers = [1,2,3,4,5]
# squared = map(lambda x: x ** 2,numbers)
# print(list(squared))

# a = [1,2,3]
# b = [4,5,6]
# combined = map(lambda x,y:x+y,a,b)
# print(list(combined))

# numbers = [10, 5, 25, 8]
# print(max(numbers))
# print(min(numbers))

# words = ["apple", "banana", "grape"]
# print(max(words))
# print(min(words))

# nums = iter([1, 2, 3, 4])
# print(next(nums))
# print(next(nums))
# print(next(nums))
# print(next(nums))

# nums = iter([1])
# print(next(nums))

# file = open("example.txt")
# print(next(file))

# a = object()
# b =  object()
# print(a == b)

# print(pow(2,3))
# print(pow(10,2))
# print(pow(5,2))


# python variables 
# x = 5
# y = 10
# print(x)
# print(y)

# x = 4 
# x = 'test'
# print(x)

# myvar = 'test'
# print(myvar)
# my_var = 'test'
# print(my_var)
# _my_var = 'test'
# print(_my_var)
# MYVAR = 'test'
# print(MYVAR)
# myvar2 = 'test'
# print(myvar2)
# x, y, z = "Orange", "Banana", "Cherry"
# print(x)
# print(y)
# print(z)

# a,b,c = 'sameet','nitesh','vishal'
# print(a)
# print(b)
# print(c)

# fruits = ["apple", "banana", "cherry"]
# print(fruits)

# x = "Python is awesome"
# print(x)

# x = "Python"
# y = "is"
# z = "awesome"
# print(x,y,z)

# x = "Python "
# y = "is "
# z = "awesome"
# print(x + y + z)

# x = 5
# y = 10
# print(x + y)

# x = 5 
# y = 'nitesh'
# print(x,y)

# x = 'awesome'
# def myfunc():
#     print('python is '+x)
# myfunc()

# x = 'nitesh'
# print(x[3])

# text = 'nitesh khatri'
# print(text[0])
# print('test')

# x = 5
# print(type(x))

# x = 'hello world'
# x = 20
# x = 20.5
# x = 1j
# x = ['apple','watermelon','grape']
# x = range(6)
# x = ('apple','watermelon','grape')
# x = range(6)
# x = {"name":"nitesh","age":"37"}
# x = {'apple','banana','cherry'}
# x = frozenset({'apple','banana','cherry'})
# x = True
# x = b"Hello"
# x = bytearray(5)
# x = memoryview(bytes(5))
# x = None
# x = 1
# x = 2.8
# x = 22j
# x = ['happy','sad','coolest','morning','breakfast']
# x = {'happy','sad','coolest','morning','breakfast'}
# x = {'name':'nitesh','age':'34'}
# x = -3255522
# x = -5j
# x = int(1)
# x = int(2.8)
# x = int('3')
# x = float("4.2")
# x = str(2)
# x = str(3.0)
# x = 'hello'
# x = 'it is alright'
# x = 'he is called "johnny"'
# x = 'he is called "johnny"'
# x = 'hello'
# x =  """Lorem ipsum dolor sit amet,
# consectetur adipiscing elit,
# sed do eiusmod tempor incididunt
# ut labore et dolore magna aliqua."""
# x = 'hello world'
# x = 'hello world'
# for x in 'apple':
#     print(x)
# for example in 'pineapple':
#     print(example)
# a = 'hello world'
# print(len(a))
# txt = "The best things in life are free!"
# print('free' in txt)
# txt = "The best things in life are free!"
# if "free" in txt:
#     print("yes, 'free' is present.")
# txt ='how are you'
# if "how" in txt: 
#     print("yes, 'how' is present")
# txt = "The best things in life are free!"
# print('wonderful' not in txt)
# txt = 'how are you feeling'
# if 'expensive' and 'happy' not in txt: 
#     print("no,'expensive' & 'happy' is NOT present.")
# txt = 'what do you want to know'
# if 'unhappy' and 'happy' not in txt:
#  print("no, 'unhappy' & 'happy', two words isn't present. ")
# if('apple' in fruitswise):
#     print('yes, there is an including "apple"')

# fruitswise1 = ['apple','banana','watermelon']
# print(fruitswise1[-1])

# teamwise = ['pawan','prathmesh','koushik','nitesh']
# if 'pawan' not in teamwise or 'prathmesh' not in teamwise:
#     print("No, 'pawan' and 'prathmesh' aren't present.")

# fruits = ['apple', 'banana', 'cherry']
# newlist = ['apple' for x in fruits]
# print(newlist)

# list1 = ['a', 'b' , 'c']
# list2 = [1, 2, 3]
# def example():
#     for x in list2:
#         list1.append(x)
#     return list1
# result = example()
# print(result)

# print("Content that you wanna print on screen")

# fruits = ('apple', 'banana', 'cherry','mango')
# (x, b,*y) = fruits
# print(y)

# for x in ('apple', 'banana', 'cherry'):
#     print(x)

# a = 50
# b = 60 
# if a == b:
#     print('yes')
# else:
#     print('no')

# set1 = {1,2,3,4,5,6}
# set2 = {2,4,6,8,10}
# print(set1.difference(set2))

# set2.difference(set1)

# print("It's alright")
# print("He is called 'Johnny'")
# print('He is called "Johnny"')

# a = "Hello"
# print(a)


# a = "Hello, World!"
# print(a[1])

# for x in "banana":
#   print(x)

# a = "Hello, World!"
# print(len(a))

# txt = "The best things in life are free!"
# print("free" in txt)

# txt = "The best things in life are free!"
# if "free" in txt:
#   print("Yes, 'free' is present.")

# print(10 > 9)
# print(10 == 9)
# print(10 < 12)


# a = 200
# b = 33

# if b > a:
#   print("b is greater than a")
# else:
#   print("b is not greater than a")

# print(bool("Hello"))
# print(bool(15))

# x = "Hello"
# y = 15
# print(bool(x))
# print(bool(y))

# print(bool("abc"))
# print(bool(123))
# print(bool(["apple", "cherry", "banana"]))

# print(bool(False))
# print(bool(None))
# print(bool(0))
# print(bool(""))
# print(bool(()))
# print(bool([]))
# print(bool({}))

# name = "Shruti"
# print(f"Hi my name is: {name}")

# var1 = input("Enter your name: ")
# print("My name is: ", var1)

# var1 = int(input("Enter the integer value: "))
# print(var1)

# var1 = float(input("Enter the float value: "))
# print(var1)

# for i in range(0, 101, 2):
#     print(i)

# """This is a
# multi-line
# comment"""

# print("Hello\nWorld")
# print('nitesh\tkhatri')
# print('nitesh\\khatri')
# print('nitesh\"khatri')
# print('nitesh\"khatri')
# print('nitesh\rkhatri')
# print('nitesh\bkhatri')

# my_list = [1, 2, 3, "hello"]
# numbers_only = [x for x in my_list if isinstance(x,(int,float))]
# print(numbers_only)

# s = {1, 2, 3}
# print(s)

# print("Hello there!\nHow are you?\nI\'m doing fine.")
# my_list = [1,2,3,4]
# result = my_list.append(5)
# print(result)


# result = my_list.insert(1, "new")
# print(my_list)

# my_tuple = (1, 2, 3)
# print(my_tuple.count(2))
# print(my_tuple.index(3))

# print(my_set = {1, 2, 3})
# print(my_set.add(4))
# print(my_set.remove(2))
# print(my_set.union({5, 6}))

# import math
# print(math.sqrt(16))

furniture = ['table', 'chair', 'rack', 'shelf']
print(furniture)