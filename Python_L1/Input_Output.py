print("Hello World")
# Python's input() function is used to take user input. By default, it returns the user input in form of a string. 
name = input("What is your name ? ")
print("Hello",name)
# If you need another data type (like integer or float), you must convert it manually using typecasting.
age = int(input("What is your age ? "))
print("Your age is",age)
print(type(age))
# Take Multiple Input in Python
a,b,c = map(float, input("Enter three subject marks : ").split())
print("a =",a)
print("b =",b)
print("c =",c)


# integer = int(input("Enter an integer : "))
# floatnumber = float(input("Enter a float number : "))
# string = input("Enter a string : ")
# complexnumber = complex(input("Enter a complex number : "))
# list1 = list(map(int, input("Enter a list of integers : ").split()))
# tuple1 = tuple(map(int, input("Enter a tuple of integers : ").split()))
# dict1 = dict(map(str, input("Enter a dictionary (key:value pairs) : ").split()))
# set1 = set(map(int, input("Enter a set of integers : ").split()))

# print("Integer:", integer)
# print("Float:", floatnumber)
# print("String:", string)
# print("Complex Number:", complexnumber)
# print("List:", list1)
# print("Tuple:", tuple1)
# print("Dictionary:", dict1)
# print("Set:", set1)