lis = [1,2,3,4];
lis2= [5,6,7,8];

# Accessing List
print(lis[1])
print(lis[-1])
# loop for list
for i in lis:
    print(i,end=" ");
# loop with index
print()
for i in range(len(lis)):
    print(lis[i], end=" ")
print()


# slicing the list
print(lis[1:3]);
print(lis[-3:-1]);

# add element on list
lis.append(5);
lis.insert(2,11);
lis.extend(lis2);
print(lis2)
print(lis)

# Remove
lis3 = [1,2,3,4]
lis3.remove(1); #  remove form specified value
print(lis3)
lis3.pop(2); # Remove and return item at index (default last). or specified index position
print(lis3)
del lis3[1];
print(lis3);
lis3.clear();
print(lis3) ; # return empty list


# list comprehension
l = [1,2,3,5,4,6,7,8,9,10];
even = [i for i in l if  i%2==0  ]
print(even)

# Sorting list
l.sort();
print(l);
l.sort(reverse=True) # descending order
print(l)

# copy list
l3 = l.copy();
print(l in l3); # False;
print(l3)

l2 = l;
print(l2 in l) # False;
print(l2);
"""
How Python Stores List Elements?

In Python, a list doesn’t store actual values directly. Instead, it stores references (pointers) to objects in memory. This means numbers, strings and booleans are separate objects in memory and the list just keeps their addresses.

That’s why modifying a mutable element (like another list or dictionary) can change the original object, while immutables remain unaffected.
"""
a = [10, 20, "GfG", 40, True]
print(a)
print(a[0])
print(a[1])
print(a[2])

# Explanation:
# The list a contains an integer (10, 20 and 40), a string ("GfG") and a boolean (True).
# Elements are accessed using indexing (a[0], a[1], etc.).
# Each element keeps its original type.