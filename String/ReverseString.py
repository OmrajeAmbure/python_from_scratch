def reverseString(s):
    if s == None:
        return s;
    rev  = [];
    n = len(s)
    for i in range(1,n+1):
        rev.append(s[- i]);
    return "".join(rev);


# def numberReverse(n):
#     if n == 0:
#         return 0;
#     rev = 0;
#     while n != 0:
#         lastDigit = n % 10;
#         rev =  rev * 10 + lastDigit;
#         n =  n // 10
#     return rev

# reverseString("nayan");
print(reverseString("omraje"));
# print(numberReverse(124));
