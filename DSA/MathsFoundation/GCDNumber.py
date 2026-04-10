def GCDNumber(a,b):
    # if a==0 and b==0:
    #     return max(a,b);
    # result = min(a,b);
    # while result>0:
    #     if a%result==0 and b%result==0:
    #         break;
    #     result-=1;
    # return result;
    if b==0:
        return a;
    while b!=0:
        a,b = b,a%b;
    return a;

def LCMNumber(a,b):
    g = max(a,b);
    s = min(a,b);
    for i in range(g,a*b+1,g):
        if i % s == 0:
            return i;
    return a * b;

print(GCDNumber(10,12));
# print(GCDNumber(24,15))
print(LCMNumber(5,11));