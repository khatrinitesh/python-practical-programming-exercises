# name = 'hello world'
# age = 35
# city = 'mumbai'
# print(name,age,city)
# print(f"{name}, you are {age} years old, {city}")

# x = 10
# y = 20
# print(f'multiplication',x*y)
# print(f'addition',x+y)
# print(f'subtraction',x-y)
# print(f'division',x/y)
# print(f'modules',x%y)

# 1. clear() Assignment: Remove all elements from the dictionary.
# student = {
#     "name": "John",
#     "age": 25,
#     "course": "Python"
# }
# print(student)

# copy() Assignment: Create a copy of the dictionary and add a new key to the copied dictionary.
# student = {
#     "name": "John",
#     "age": 25
# }
# student_copy = student.copy()
# print(student_copy)

# fromkeys() Assignment: Create a dictionary using the following keys, with "Pending" as the value.
# subjects = ["Python", "JavaScript", "React"]
# result = dict.fromkeys(subjects,"Pending")
# print(result)

# get() Assignment: Get the value of "email" from the dictionary.
# user = {
#     "name": "David",
#     "email": "david@example.com",
#     "age": 30
# }
# email = user.get('email')
# print(email)

# student = {
#     "name": "Alex",
#     "age": 28,
#     "city": "Delhi"
# }
# for key,value in student.items():
#     print(key,value)

# keys() Assignment: Get all the keys from the dictionary.
# student = {
#     "name": "Alex",
#     "age": 28,
#     "city": "Delhi"
# }
# product = student.keys()
# print(product)

# pop() Assignment: Remove the "age" key from the dictionary.
# user = {
#     "name": "John",
#     "age": 25,
#     "city": "Mumbai"
# }
# user.pop('age')
# print(user)

# popitem() Assignment: Remove the last inserted key-value pair.
# employee = {
#     "id": 101,
#     "name": "David",
#     "department": "IT"
# }
# employee.popitem()
# print(employee)

# setdefault() Assignment: Add "city": "Mumbai" only if the "city" key does not already exist.
# user = {
#     "name": "Alex",
#     "age": 28
# }
# user.setdefault('city','mumbai')
# user.setdefault('location','grant road')
# user.setdefault('mobile no','1234567890')
# user.setdefault('pincode','400008')
# user.setdefault('state','maharashtra')
# user.setdefault('address','lamingaton road')
# print(user)

# update() Assignment: Update the user's age and add their city.
# user = {
#     "name": "John",
#     "age": 25
# }
# user.update({
#     "age":35,
#     "city":"mumbai"
# })
# print(user)

# values() Assignment: Get all values from the dictionary.
# student = {
#     "name": "David",
#     "age": 30,
#     "course": "Python"
# }
# result = student.values()
# print(result)

# numbers = (10, 20, 30, 20, 40, 20, 50)
# fruitwise = ('apple','mango','pineapple','grape','watermelon','apple')
# resultNumberWise = numbers.count(20)
# resultFruitWise = fruitwise.count('apple')
# print('Numberwise ',resultNumberWise)
# print('Fruitwise',resultFruitWise)

# index() Assignment: Find the position of the value 30 in the tuple.
# numbers = (10, 20, 30, 40, 50)
# resultNumberWise = numbers.index(20)
# print(resultNumberWise)
# fruitwise = ('apple','mango','pineapple','grape','watermelon','apple')
# resultFruitWise = fruitwise.index('grape')
# print(resultFruitWise)

# add() Assignment: Add "Mango" to the set.
# fruits = {"Apple", "Banana", "Orange"}
# fruits.add("Mango")
# fruits.add("Pineapple")
# print(fruits)

# clear() Assignment: Remove all elements from the set.
# numbers = {10, 20, 30, 40}
# numbers.clear()
# print(numbers)

# copy() Assignment: Create a copy of the set and add 50 to the copied set.
# numbers = {10, 20, 30, 40}
# numbers_copy = numbers.copy()
# numbers_copy.add(50)
# numbers_sorted = sorted(numbers_copy,reverse=False)
# print(numbers_sorted)

# difference() Assignment: Find the elements that exist in set1 but not in set2.
# set1 = {10, 20, 30, 40}
# set2 = {30, 40, 50, 60}
# setDiff = set1.difference(set2)
# print(setDiff)

# difference_update() Assignment: Remove all elements from set1 that are also present in set2.
# set1 = {10, 20, 30, 40}
# set2 = {30, 40, 50, 60}
# # set1.difference_update(set2)
# print(set1)
# print('Ascending',sorted(set1,reverse=False))
# print(sorted('',set1,reverse=True))

# discard() Assignment: Remove 30 from the set using discard().
# numbers = {10, 20, 30, 40}
# numbers.discard(30)
# numbers.discard(100)
# print(sorted(numbers))
# print(sorted(numbers,reverse=True))

# intersection() Assignment: Find the common elements between two sets.
# set1 = {10, 20, 30, 40}
# set2 = {30, 40, 50, 60}
# result = set1.intersection(set2)
# result = sorted(set1.intersection(set2),reverse=True)
# print(result)

# set1 = {10, 20, 30, 40}
# set2 = {30, 40, 50, 60}
# set1.intersection_update(set2)
# print(set1)

# issubset() Assignment: Check whether all elements of set1 are present in set2.
# set1 = {10, 20}
# set2 = {10, 20, 30, 40}
# result = set1.issubset(set2)
# print(result)
# set3 = {'a','b'}
# set4 = {'c','d','a'}
# result = set3.issubset(set4)
# print(result)

# issuperset() Assignment: Check whether set1 contains all elements of set2.
# set1 = {10, 20, 30, 40}
# set2 = {10, 20}
# result = set1.issuperset(set2)
# print(result)

# pop() Assignment: Remove an element from the set using pop() and store the removed value in result.
# numbers = {10, 20, 30, 40}
# result = numbers.pop()
# print(result)

# remove() Assignment: Remove 30 from the set using remove().
# numbers = {10, 20, 30, 40}
# numbers.remove(30)
# print(numbers)
# print(sorted(numbers,reverse=True))

# symmetric_difference() Assignment: Find the elements that exist in either set, but not in both.
# set1 = {10, 20, 30}
# set2 = {30, 40, 50}
# result = set1.symmetric_difference(set2)
# print(result)

# symmetric_difference_update() Assignment: Update set1 with the symmetric difference of set1 and set2.
# set1 = {10, 20, 30}
# set2 = {30, 40, 50}
# set1.symmetric_difference_update(set2)
# print(set1)

# union() Assignment: Combine the elements of both sets without duplicates.
# set1 = {10, 20, 30}
# set2 = {30, 40, 50}
# result = set1.union(set2)
# print(sorted(result))

# update() Assignment: Add all elements from set2 into set1.
# set1 = {10, 20, 30}
# set2 = {30, 40, 50}
# result = set1.update(set2)
# print(set1)
# print(sorted(set1))

# intersection
# result = students_python.intersection(students_java)
# print(result)
# difference
# result = students_python.difference(students_java)
# print(result)
# result = students_java.difference(students_python)
# print(result)
# result = students_python.union(students_java)
# print(result)
# result = "John" in students_python
# print(result)
# students_python.add('Emma')
# print(sorted(students_python,reverse=True))
# students_python.discard('Mike')
# print(students_python)
# result = students_python.issuperset({"John","David"})
# print(result)
# students_copy  = students_python.copy()
# print(students_copy )
# students_copy = students_python.copy()
# students_copy.clear()
# print(students_copy)
# students_python = {"John", "David", "Alex", "Mike"}
# students_java = {"David", "Alex", "Robert", "Sarah"}

# Python File Methods — Assignment Below are practical assignments for Python file methods. Try solving each one yourself before checking the expected output.
# close Assignment: Open a file and close it using close().
# file = open('sample.txt','w')
# file.write('hello python')
# print(file.closed)

# read() Assignment: Read the complete contents of a file using read().
# file = open('sample2.txt','r')
# content = file.read()
# print(content)
# print(file)

# readable() Assignment: Check whether the file can be read.
# file = open('sample3.txt','r')
# content = file.read()
# print(content)

# file = open("sample.txt", "r")
# line = file.readline()
# print(line)
# file.close()

# readlines() Assignment: Read all lines from the file and store them in a list.
# file = open('sample.txt','r')
# lines = file.readlines()
# print(lines)
# file.close()

# write() Assignment: Create a file called student.txt and write the following text:
# file = open('student.txt','w')
# file.write('name: john\nAge: 25\nCourse:Python')
# file.close()

# students = [
#     "John\n",
#     "David\n",
#     "Alex\n"
# ]
# file = open('students.txt','w')
# file.writelines(students)
# file.close()

# tell() Assignment: Find the current position of the file cursor using tell().
# file = open('sample.txt','w')
# content = file.read()
# position = file.tell()
# print(position)
# file.close()

# seek() Assignment: Move the file cursor to the beginning of the file and read the content again.
# file = open('sample.txt','r')
# content1 = file.read()
# file.seek(0)
# content2 = file.read()
# print(content1)
# print(content2)

# seekable() Assignment: Check whether the file allows the cursor position to be changed.
# file = open('sample.txt','r')
# result = file.seekable()
# print(result)
# file.close()

# file = open('example1.txt','w')
# result = file.write('hi example')
# print(result)
# file.close()


# flush() Assignment: Write data to a file and manually flush the internal buffer.
# file = open("sample.txt", "w")
# file.write('hello python')
# file.close()

# truncate() Assignment: Resize the file so that only the first 5 characters remain.
# file = open('sample.txt','r')
# file.close()
# print(file)

# detach() Assignment: Open a file in binary mode and separate the underlying raw stream from the buffered object.