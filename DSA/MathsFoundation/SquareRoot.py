def SquareRoot(n):
    res = 1;
    while res*res <= n:
        res += 1;
    return res-1;

# def floorSqrt(n):

if __name__=="__main__":
    print(SquareRoot(9));