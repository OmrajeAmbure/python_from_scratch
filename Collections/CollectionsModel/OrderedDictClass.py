from collections import  OrderedDict;
"""
OrderedDict
An OrderedDict is a dictionary that preserves the order in which keys are inserted. While regular dictionaries do this from Python 3.7+, OrderedDict also offers extra features like moving re-inserted keys to the end making it useful for order-sensitive operations.
"""
print("This is a Dict:\n")
d = {}
d['a'] = 1;
d['b'] = 2;
d['c'] = 3;
d['d'] = 4;
for k,v in d.items():
    print(k,v);

print("\nThis is an Ordered Dict:\n");
od = OrderedDict()
od['a'] = 1
od['b'] = 2
od['c'] = 3
od['d'] = 4
for key, value in od.items():
    print(key, value)
# deleting element
od.pop('a')

# Re-inserting the same
od['a'] = 10
print()
for key, value in od.items():
    print(key, value)

"""
DefaultDict
A DefaultDict is also a sub-class to dictionary. It is used to provide some default values for the key that does not exist and never raises a KeyError.
default_factory is a function that provides the default value for the dictionary created. If this parameter is absent then the KeyError is raised.

Initializing DefaultDict Objects
DefaultDict objects can be initialized using DefaultDict() method by passing the data type as an argument.
"""

from collections import defaultdict
d = defaultdict(int);
L = [1, 2, 3, 4, 2, 4, 1, 2]

# Counting occurrences of each element in the list
for i in L:
    d[i] += 1  # No need to check key existence; default is 0

print(d)

from collections import defaultdict

# Defining a dict
d = defaultdict(list)

for i in range(5):
    d[i].append(i)

print("Dictionary with values as list:")
print(d)

"""
ChainMap
A ChainMap encapsulates many dictionaries into a single unit and returns a list of dictionaries.
"""
from collections import ChainMap

d1 = {'a': 1, 'b': 2}
d2 = {'c': 3, 'd': 4}
d3 = {'e': 5, 'f': 6}

# Defining the chainmap
c = ChainMap(d1, d2, d3)
print(c)

"""
Accessing Keys and Values from ChainMap
Values from ChainMap can be accessed using the key name. They can also be accessed by using the keys() and values() method.
"""
from collections import ChainMap

d1 = {'a': 1, 'b': 2}
d2 = {'c': 3, 'd': 4}
d3 = {'e': 5, 'f': 6}

# Defining the chainmap
c = ChainMap(d1, d2, d3)

# Accessing Values using key name
print(c['a'])

# Accessing values using values()
print(c.values())

# Accessing keys using keys()
print(c.keys())

"""
Adding new dictionary
A new dictionary can be added by using the new_child() method. The newly added dictionary is added at the beginning of the ChainMap.
"""

import collections

# initializing dictionaries
dic1 = {'a': 1, 'b': 2}
dic2 = {'b': 3, 'c': 4}
dic3 = {'f': 5}

# initializing ChainMap
chain = collections.ChainMap(dic1, dic2)

# printing chainMap
print("All the ChainMap contents are: ")
print(chain)

# using new_child() to add new dictionary
chain1 = chain.new_child(dic3)

# printing chainMap
print("Displaying new ChainMap : ")
print(chain1)