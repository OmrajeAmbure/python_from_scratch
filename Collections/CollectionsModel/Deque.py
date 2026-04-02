from  collections import deque
"""
Deque (Doubly Ended Queue) is the optimized list for quicker append and pop operations from both sides of the container. It provides O(1) time complexity for append and pop operations as compared to list with O(n) time complexity.
Syntax:
class collections.deque(list)
"""
queue = deque(['name','age','DOB']);
print(queue)

"""
Inserting Elements
Elements in deque can be inserted from both ends. To insert the elements from right append() method is used and to insert the elements from the left appendleft() method is used.
"""

from collections import deque

# Initializing deque with initial values
de = deque([1, 2, 3])

# Append 4 to the right end of deque
de.append(4)

# Print deque after appending to the right
print("The deque after appending at right is :")
print(de)

# Append 6 to the left end of deque
de.appendleft(6)

# Print deque after appending to the left
print("The deque after appending at left is :")
print(de)

"""
Removing Elements
Elements can also be removed from the deque from both the ends. To remove elements from right use pop() method and to remove elements from the left use popleft() method.
"""
from collections import deque

# Initialize deque with initial values
de = deque([6, 1, 2, 3, 4])

# Delete element from the right end (removes 4)
de.pop()

# Print deque after deletion from the right
print("The deque after deleting from right is :")
print(de)

# Delete element from the left end (removes 6)
de.popleft()

# Print deque after deletion from the left
print("The deque after deleting from left is :")
print(de)