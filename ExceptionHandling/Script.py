print("Division Operation Started ");

"""
📝 Exception Handling : 
        - Exception Handling allows a program to gracefully handle unexpected events (like invalid input or missing files) without crashing. Instead of terminating abruptly, Python lets you detect the problem, respond to it, and continue execution when possible.
        Syntax:- 
                try:
                    # Code 
                except SomeException:
                    # Code 
                else:
                    # Code 
                finally:
                    # Code 
    ◉ try: Runs the risky code that might cause an error.
    ◉ except: Catches and handles the error if one occurs.
    ◉ else: Executes only if no exception occurs in try.
    ◉ finally: Runs regardless of what happens useful for cleanup tasks like closing files.
📝 Difference Between Errors and Exceptions
Errors and exceptions are both issues in a program, but they differ in severity and handling.
        – Error: Issues in the program logic such as SyntaxError, etc. It occurs at compile time.
        – Exception: Problems that occur at runtime and can be managed using exception handling (e.g., invalid input, missing files).
"""

try:
    n1, n2 = input("Enter The Number want to Divide (format: n1 ➗ n2 ):- ").split(" ");
    res = int(n1)/int(n2);
except ZeroDivisionError:
    print("Zero Division Exception ")
except (ValueError,TypeError) as e: # Catching Multiple Exceptions
    print(e)
else:
    print("Result is ",res);
finally:
    print("Division Operation Completed")


"""
📝 Python Built-in Exceptions :- 
       - Python provides a set of built-in exceptions, each designed to signal a specific type of error and help you debug more effectively.
       1. BaseException :
            - The BaseException class is the root of Python's exception hierarchy. All other exceptions directly or indirectly inherit from it. 
            While it is rarely used directly in code, it is important because it forms the foundation of Python’s error-handling system
            try:
                raise BaseException("This is a BaseException")
            except BaseException as e:
                print(e)
       2. Exception :
            - The Exception class is the base for all non-exit exceptions. You will often catch Exception in general 
            error-handling code when you are not targeting a specific error type.
            Example: This code raises a generic Exception and handles it inside the except block.
            try:
                raise Exception("This is a generic exception")
            except Exception as e:
                print(e)
        3. ArithmeticError :
            - The ArithmeticError class is the base for all errors related to mathematical operations. You don’t usually raise it directly,
             but it provides a way to catch all math-related errors in one block.
            Example: This example raises an ArithmeticError manually to demonstrate how it works.
            try:
                    raise ArithmeticError("Arithmetic error occurred")
            except ArithmeticError as e:
                    print(e)
        4. ZeroDivisionError :
            - A ZeroDivisionError occurs when you attempt to divide a number by zero. Since division by zero is undefined in mathematics, 
            Python raises this exception to signal the error.
            Example: This code attempts to divide 10 by 0, which triggers a ZeroDivisionError.
            try:
                result = 10 / 0
            except ZeroDivisionError as e:
                print(e)
        5. OverflowError :
            - An OverflowError occurs when the result of a numerical operation is too large for Python to represent. 
            While Python handles large integers well, certain floating-point operations (like very large exponentials) can still cause this error.
            Example: This example uses the math.exp() function with a very large input, which causes an overflow.
            import math
            try:
                result = math.exp(1000)  # Exponential function with a large argument
            except OverflowError as e:
                print(e)
        6.  FloatingPointError
            - The FloatingPointError occurs when a floating-point calculation fails. By default, Python handles most floating-point issues silently (like dividing by zero results in inf or nan). 
            However, you can explicitly enable floating-point error reporting with libraries like NumPy.
            Example: This example enables error reporting in NumPy and performs a division by zero to trigger FloatingPointError.
            import numpy as np
            np.seterr(all='raise')
            try:
                np.divide(1, 0)
            except FloatingPointError as e:
                print("FloatingPointError caught:", e)
        7. AssertionError :
            - An AssertionError is raised when the assert statement fails. The assert keyword is often used for debugging or testing assumptions in code.
            Example: This example checks if 1 == 2 using assert. Since the condition is false, it raises an AssertionError.
            try:
                assert 1 == 2, "Assertion failed"
            except AssertionError as e:
                print(e)
        8. AttributeError  : 
            - An AttributeError occurs when you try to access or assign an attribute that does not exist for an object.
            Example: This example tries to access a non-existent attribute in a class instance
            class MyClass:
                pass
            obj = MyClass()
            try:
                obj.some_attribute
            except AttributeError as e:
                print(e)
        9. IndexError:
            - An IndexError happens when you try to access a list (or any sequence) element with an index that is out of range.
            Example: This example tries to access the 6th element of a list that only has 3 elements.
            my_list = [1, 2, 3]
            try:
                element = my_list[5]
            except IndexError as e:
                print(e)
        10. KeyError :
            - A KeyError occurs when you try to access a dictionary key that doesn’t exist.
            Example: This example tries to access the key "key2" in a dictionary that only has "key1".
            d = {"key1": "value1"}
            try:
                    val = d["key2"]
            except KeyError as e:
                    print(e)
        11. MemoryError :
            - A MemoryError occurs when Python cannot allocate enough memory for an operation. This usually happens when trying to create extremely large data structures.
            Example: This example tries to create a very large list, which may exceed memory limits.
            try:
                li = [1] * (10**10)
            except MemoryError as e:
                print(e)
        12. NameError :
            - A NameError occurs when you use a variable or function name that has not been defined.
            Example: This example tries to print a variable that was never declared.
            try:
                print(var)
            except NameError as e:
                print(e)
        13. OSError (and related errors)
            - Raised when a system-related operation (like file I/O, opening files, or interacting with the OS) fails. 
            In Python 3:
                    ● IOError is just an alias for OSError (they are the same).
                    ● FileNotFoundError is a subclass of OSError, specifically raised when a file or directory does not exist.
            Example: This example attempts to open a missing file, which triggers FileNotFoundError (a subclass of OSError).
            try:
                open("non_existent_file.txt")  # File does not exist
            except FileNotFoundError as e:     # More specific
                print("FileNotFoundError caught:", e)
            except OSError as e:               # General OS-related error
                print("OSError caught:", e)
"""


"""
Raise an Exception
        - We raise an exception in Python using the raise keyword followed by an instance of the exception class that we want to trigger. 
        We can choose from built-in exceptions or define our own custom exceptions by inheriting from Python's built-in Exception class.
        Basic Syntax:
            raise ExceptionType("Error message")
"""
def set(age):
    if age < 0:
        raise ValueError("Age cannot be negative.")
    print(f"Age set to {age}")
try:
    set(-5)
except ValueError as e:
    print(e)

set(23)