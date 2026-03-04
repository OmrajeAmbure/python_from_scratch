def gcd(m,n):
    fm = [];
    for i in range(1,m+1):
        if m%i==0:
            fm.append(i);
    fn = [];
    for j in range(1,n+1):
        if n%j == 0:
            fn.append(j)
    cf = [];
    for f in fn:
        if f in fm:
            cf.append(f);
    return (cf[-1]);

def better_approach_gcd(m,n):
    cf = [];
    for  i in range(1,min(m,n)+1):
        if m%i==0 and n%i==0:
            cf.append(i);
    return (cf[-1]);

def gcd_using_euclidean_algorithm(m,n):
    while n:
        m, n = n, m % n
    return m

gcd = gcd(14,63);
print(gcd);
better_gcd = better_approach_gcd(14,63);
print(better_gcd);
print(gcd_using_euclidean_algorithm(14,63));