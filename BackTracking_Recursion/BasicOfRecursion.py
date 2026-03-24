def printN(n):
    if n == 0:
        return ;
    print(n , end=" | ") # Before The Recursion call
    printN(n - 1);

    print(n , end=" | ") # After The Recursion call
printN(8);