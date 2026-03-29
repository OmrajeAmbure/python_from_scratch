def doubleTup(numbers):
    t = ();
    for i in range(len(numbers)):
        t = t + (numbers[i]*2,) ;
    return t;
print(doubleTup((4,5,1,2,3,5)));