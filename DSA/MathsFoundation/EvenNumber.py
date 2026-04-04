def EvenOdd(n):
    if n%2==0:
        return True;
    else:
        return False;

def EvenOddAndOperator(n):
    if n & 1 == 0:
        return True;
    else:
        return False;

if __name__ == "__main__":
    n = 13;
    if EvenOdd(n):
        print("Even Number");
    else:
        print("Odd Number")