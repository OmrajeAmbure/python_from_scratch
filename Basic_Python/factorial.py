# by using recursion
def factorial(n):
    if n==0 or n==1:
        return 1;
    else:
        return n*factorial(n-1);

print(factorial(5));
print(factorial(4));

# by using For Loop

def factorial(n):
    factorial = 1
    for i in range(1,n+1):
        factorial = factorial*(i)
    return factorial;

print(factorial(5))


# By using The While Loop

fact = 1;
n = 5
while n > 0:
    fact = fact * n;
    n = n - 1;
print(fact)