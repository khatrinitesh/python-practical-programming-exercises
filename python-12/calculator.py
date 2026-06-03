print('simple calculator')
print('1. addition')
print('2. subtraction')
print('3. multiplication')
print('4. division')
print('5. modulus')
print('6. exponentiation')

choice = input('enter your choice: ')

n1 = float(input('enter first number: '))
n2 = float(input('enter second number: '))

if choice == "1":
    result = n1 + n2
    print('Result:',result)
elif choice == "2":
    result = n1 - n2
    print('Result:',result)
elif choice == "3":
    result = n1 * n2 
    print('Result:',result)
elif choice == "4":
    if n2 == 0:
        print('cannot divide by zero')
    else:
        result = n1 / n2
        print('Result:',result) 
elif choice == "5":
    result = n1 %  n2
    print('Result:',result)
elif choice == "6":
    result = n1 ** n2
    print('Result:',result)
else:
    print('invalid choice')