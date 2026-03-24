# In Python, a string is a sequence of characters written inside quotes. It can include letters, numbers, symbols and spaces.
# - Python does not have a separate character type.
# - A single character is treated as a string of length one.
# - Strings are commonly used for text handling and manipulation.

# Creating String
s1 = 'HELLO'
s2 = "hello"
s3 = """\nhello my name is omraje . \nI am live in pune , my current qualification is BE in AI&DS """
print(s1)
print(s2)
print(s3)

# Accessing characters in String
#   --> it is collection of character , it will be Accessing through positive(Start with 0 to n) or negative (start with -1 to -n) indexing
# | H | E | L | L | O |
print(s3[1]) # space is calculate as 0 position " \n "
print(s1[-1])
print(s1[-3])
# Note: Accessing an index out of range will cause an IndexError. Only integers are allowed as indices and using a float or other types will result in a TypeError.

# String Slicing
# --> Slicing is a way to extract a portion of a string by specifying the start and end indexes. The syntax for slicing is string[start:end], where start starting index and end is stopping index (excluded).
# Syntax :  substring = s[start : end : step]
# Parameters:
#                   s: The original string.
#                   start (optional): Starting index (inclusive). Defaults to 0 if omitted.
#                   end (optional): Stopping index (exclusive). Defaults to the end of the string if omitted.
#                   step (optional): Interval between indices. A positive value slices from left to right, while a negative value slices from right to left. If omitted, it defaults to 1 (no skipping of characters).
print(s3[0:14]) #  output :- "hello my name"
print(s3[-12:-1]) # output :- "BE in AI&DS"
print(s1[::-1]) # output :- "OLLEH"
print(s1[1::-1])