# A Set in Python is used to store a collection of items with the following properties.

# No duplicate elements. If try to insert the same item again, it overwrites previous one.
# An unordered collection. When we access all items, they are accessed without any specific order and we cannot access items using indexes as we do in lists.
# Internally use hashing that makes set efficient for search, insert and delete operations. It gives a major advantage over a list for problems with these operations.
# Mutable, meaning we can add or remove elements after their creation, the individual elements within the set cannot be changed directly.

s = {10, 50, 20}
print(s)
print(type(s))

# typecasting list to set
s = set(["a", "b", "c"])
print(s)

# Adding element to the set
s.add("d")
print(s)

# a set cannot have duplicate values
s = {"Geeks", "for", "Geeks"}
print(s)

# values of a set cannot be changed
s[1] = "Hello"
print(s)

# Output

# {'Geeks', 'for'}
# TypeError: 'set' object does not support item assignment

# Heterogeneous Element in a set
s = {"Geeks", "for", 10, 52.7, True}
print(s)

# Frozen Sets
# A frozenset is an immutable version of a set. Its elements cannot be changed after creation, but you can perform operations like union, intersection and difference. Use frozenset() to create one.

# Normal set (mutable)
s = set(["a", "b", "c"])
print("Normal Set:", s)
# Frozen set (immutable)
fs = frozenset(["e", "f", "g"])
print("Frozen Set:", fs)

# Output
('Normal Set:', set(['a', 'c', 'b']))
('Frozen Set:', frozenset(['e', 'g', 'f']))
# Note: Frozensets are immutable, so methods like add() or remove() cannot be used. They are also hashable, which allows them to be used as dictionary keys.

# Internal working of Set
# This is based on a data structure known as a hash table.  If Multiple values are present at the same index position, then the value is appended to that index position, to form a Linked List.

# In, Python Sets are implemented using a dictionary with dummy variables, where key beings the members set with greater optimizations to the time complexity.

# The diagram shows how Python internally manages collisions in sets using linked lists for efficient element storage and retrieval.

# Each index in the hash table represents a possible hash value where elements are stored based on their computed hash key.
# When two elements map to the same index, they are linked together using a linked list, forming a chain at that position.
# This chaining mechanism helps efficiently handle collisions, allowing multiple elements to exist at the same hash index without overwriting each other.
# Sets with Numerous operations on a single HashTable:
# The hash table stores elements based on their computed index values for example, values 20 and 30 are placed at index 5, while 40 goes to index 6 and 50 to index 8. When multiple values share the same index, they are linked together, forming a chain (as seen at index 5).

# During traversal, insertion or deletion, the algorithm moves through these linked elements at each index to access or modify data efficiently.

# Methods for Sets
# 1. Adding elements to Sets: add() function is used to insert new elements into a set. It automatically ignores duplicates.




s = {"a", "b", "c"}
s.add("d")
print(s)

# Output
# {'c', 'd', 'a', 'b'}
# 2. Union of Sets: union() function combines two sets and returns a new set with all unique elements.




a = {"x", "y"}
b = {"y", "z"}
u = a.union(b)
print(u)

# Output
# {'z', 'y', 'x'}
# 3. Intersection of Sets: intersection() function returns a new set containing elements that are common to both sets.




a = {1, 2, 3}
b = {2, 3, 4}
i = a.intersection(b)
print(i)

# Output
# {2, 3}
# 4. Difference of Sets: difference() function returns a set containing elements that are in the first set but not in the second.




a = {1, 2, 3}
b = {2, 3, 4}
d = a.difference(b)
print(d)

# Output
# {1}
# 5. Clearing a Set: clear() function removes all elements from a set, leaving it empty.




s = {1, 2, 3}
s.clear()
print(s)

# Output
# set()
# Operators for Sets
# Sets and frozen sets support the following operators:

# Operators	Notes
# key in s	containment check
# key not in s	non-containment check
# s1 == s2	s1 is equivalent to s2
# s1 != s2	s1 is not equivalent to s2
# s1 <= s2	s1 is subset of s2
# s1 < s2	s1 is proper subset of s2
# s1 >= s2	s1 is superset of s2
# s1 > s2	s1 is proper superset of s2
# s1 | s2	the union of s1 and s2
# s1 & s2	the intersection of s1 and s2
# s1 - s2	the set of elements in s1 but not s2
# s1 ˆ s2	the set of elements in precisely one of s1 or s2
