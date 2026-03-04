# In Python, variables are used to store data that can be referenced and manipulated during program execution. A variable is essentially a name that is assigned to a value.

# Unlike Java and many other languages, Python variables do not require explicit declaration of type.
# The type of the variable is inferred based on the value assigned.

# Memory Concept:-  https://chatgpt.com/share/6988cc27-b480-8012-b6af-aabf4722ce52 

x = 5
name = "samantha"

print(x)          # Output: 5
print(name)       # Output: samantha
print(type(x))    # Output: <class 'int'>
print(type(name)) # Output: <class 'str'>

# Rules for Naming Variables
# To use variables effectively, we must follow Python’s naming rules:

# Variable names can only contain letters, digits and underscores (_).
# A variable name cannot start with a digit.
# Variable names are case-sensitive like myVar and myvar are different.
# Avoid using Python keywords like if, else, for as variable names.

## Valid variable names
age = 21
_colour = "lilac"
total_score = 90

## Invalid variable names
# 1name = "Error"  # Starts with a digit
# class = 10       # 'class' is a reserved keyword
# user-name = "Doe"  # Contains a hyphen

# Operators can also be used with variables
