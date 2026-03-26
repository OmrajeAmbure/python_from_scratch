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


"""
String Methods
Python has a set of built-in methods that you can use on strings.

Note: All string methods return new values. They do not change the original string.

Method	Description
capitalize()	Converts the first character to upper case
casefold()	Converts string into lower case
center()	Returns a centered string
count()	Returns the number of times a specified value occurs in a string
encode()	Returns an encoded version of the string
endswith()	Returns true if the string ends with the specified value
expandtabs()	Sets the tab size of the string
find()	Searches the string for a specified value and returns the position of where it was found
format()	Formats specified values in a string
format_map()	Formats specified values in a string
index()	Searches the string for a specified value and returns the position of where it was found
isalnum()	Returns True if all characters in the string are alphanumeric
isalpha()	Returns True if all characters in the string are in the alphabet
isascii()	Returns True if all characters in the string are ascii characters
isdecimal()	Returns True if all characters in the string are decimals
isdigit()	Returns True if all characters in the string are digits
isidentifier()	Returns True if the string is an identifier
islower()	Returns True if all characters in the string are lower case
isnumeric()	Returns True if all characters in the string are numeric
isprintable()	Returns True if all characters in the string are printable
isspace()	Returns True if all characters in the string are whitespaces
istitle()	Returns True if the string follows the rules of a title
isupper()	Returns True if all characters in the string are upper case
join()	Joins the elements of an iterable to the end of the string
ljust()	Returns a left justified version of the string
lower()	Converts a string into lower case
lstrip()	Returns a left trim version of the string
maketrans()	Returns a translation table to be used in translations
partition()	Returns a tuple where the string is parted into three parts
replace()	Returns a string where a specified value is replaced with a specified value
rfind()	Searches the string for a specified value and returns the last position of where it was found
rindex()	Searches the string for a specified value and returns the last position of where it was found
rjust()	Returns a right justified version of the string
rpartition()	Returns a tuple where the string is parted into three parts
rsplit()	Splits the string at the specified separator, and returns a list
rstrip()	Returns a right trim version of the string
split()	Splits the string at the specified separator, and returns a list
splitlines()	Splits the string at line breaks and returns a list
startswith()	Returns true if the string starts with the specified value
strip()	Returns a trimmed version of the string
swapcase()	Swaps cases, lower case becomes upper case and vice versa
title()	Converts the first character of each word to upper case
translate()	Returns a translated string
upper()	Converts a string into upper case
zfill()	Fills the string with a specified number of 0 values at the beginning
"""