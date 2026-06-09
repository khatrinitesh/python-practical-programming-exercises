# print('hello python')

# x = 10
# y = 10
# z = x + y 
# print(z)

# fname = input('what is your first name')
# lname = input('what is your last name')
# result = fname + ' ' + lname
# print(f'Fullname {result}')

# price = float(input('what is your price?'))
# discount = float(input('what is your discount?'))
# result = price - (price * discount / 100)
# print(result)

# marks = 78
# if marks >= 90:
#     print('Grade A+')
# elif marks >= 85:
#     print('Grade B')
# elif marks >= 70:
#     print('Grade C')
# else:
#     print('Failed')

# score = 1200
# if score >= 2000:
#     print(f'yes, target is achievement')
# else:
#     print(f'no, target is not achievement')

# x = 'nitesh'
# print(type(x))
# x =111
# print(type(x))
# x = ['a','b','c']
# print(type(x))
# x = True
# print(type(x))
# x = {'name':'test','age':33}
# print(type(x))
# x = ('asdsa','adsadad')
# print(type(x))
# x = 0 
# print(type(x))

# import requests 

# url = 'https://jsonplaceholder.typicode.com/posts'
# response = requests.get(url)

# if response.status_code == 200:
#     posts = response.json()
#     for post in posts[:5]:
#         print('post id:',post['id'])
#         print('post title:',post['title']) 
#         print('post body:',post['body']) 
#         print('-' * 30)
# else:
#     print('api call failed')
#     print('Status code:',response.status_code)

# if response.status_code == 200:
#     posts = response.json()
#     for post in posts:
#         if(post['userId']) == 1:
#             print(post['title'])
# else:
#     print('Something went wrong')



# new_post = {
#      "title": "My Python API Practice",
#     "body": "I am learning how to send data using Python.",
#     "userId": 1
# }

# response = requests.post(url,json=new_post)

# if response.status_code == 201:
#     data = response.json()

#     print('successfully')
#     print('title',data['title'])
#     print('body',data['body'])
#     print('userId',data['userId'])
# else:
#     print('failed')
#     print('Status code:',response.status_code)

# new_post = {
#      "title": "My Python API Practice",
#     "body": "I am learning how to send data using Python.",
#     "userId": 1
# }

# response = requests.post(url,json=new_post)

# if response.status_code == 201:
#     data = response.json()

#     print('successfully')
#     print('title',data['title'])
#     print('body',data['body'])
#     print('userId',data['userId'])
# else:
#     print('failed')
#     print('Status code',response.status_code)

# import requests

# url = 'https://jsonplaceholder.typicode.com/posts'

# keyword = input('enter keyword to search:').lower()

# response = requests.get(url)

# if response.status_code == 200:
#     posts = response.json()

#     found_posts = []

#     for post in posts:
#         title = post['title'].lower()

#         if keyword in title:
#             found_posts.append(post)
#     if len(found_posts) > 0:
#         print(f'found {len(found_posts)} posts:\n')

#         for post in found_posts:
#             print('ID',post['id'])
#             print('Title:',post['title'])
#             print('-' * 30)
# else:
#     print('no posts found with this keyword')
#     print('status code',response.status_code)
