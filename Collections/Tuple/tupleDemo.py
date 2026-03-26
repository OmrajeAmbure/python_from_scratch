from pygments.styles.dracula import green, yellow

t = (1,2,3,4,4,"om","vinay",True); # ordered, unchangeable(immutable) or Allow to duplicate

# Accessing Element
thistuple = tuple(("apple", "banana", "cherry"));
print(thistuple)
print(thistuple[1])
print(thistuple[:-1])
print(thistuple[::-1])
thistuple2 = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])
# Note: The search will start at index 2 (included) and end at index 5 (not included)
for i in thistuple2:
    if ("apple" == i):
        print("Yes i found the apple in tuple");

# Note1 :- To create a tuple with only one item, you have to add a comma after the item, otherwise Python will not recognize it as a tuple.
tup = ("om");
print(type(tup)) # <class 'str'>
tup1 = ("om",);
print(type(tup1)) # <class 'tuple'>

# Note2 :- we can change the tup to by converting the tuple into the list
lis = list(tup1);
lis.append("raj");
changedTuple = tuple(lis)
print(changedTuple)

# Unpacking a tuple:
fruits = ("apple", "banana", "cherry")
(green,yellow,red) = fruits;
print(green)
print(yellow)
print(red)

# method
fruits = ("apple","apple", "banana", "cherry")
print(fruits.count("apple")); # 2
print(fruits.index("banana")) # 2

tup = (0, 1, 2, 3, 4)
del tup
# print(tup) NameError: name 'tup' is not defined

