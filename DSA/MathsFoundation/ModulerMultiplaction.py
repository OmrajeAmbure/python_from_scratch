def ModulerMultiplaction(a,b,m):
    s1 = (a%m) ;
    s2 = (b%m);
    s3 = s1 * s2;
    return  s3 % m;
if __name__=="__main__":
    print(ModulerMultiplaction(5,3,11));
    print(ModulerMultiplaction(12,15,7));