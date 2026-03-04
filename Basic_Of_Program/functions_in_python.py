def demo(*args):
    print(args)
def demo_kargs(**kwargs):
    for k,v in kwargs.items():
        print(f"key:{k} value: {v}");
print(demo(2,3,4,5))
print(demo_kargs(a=3,b=4,c=5))

