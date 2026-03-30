# Taking input and initializing dictionary
keys = input().split()
values = map(int, input().split())
my_dict = dict(zip(keys, values))
k, v = input().split()
v = int(v)
# Insert k,v in my_dict
my_dict[k] = v;
print("Inserted");

# Print Inserted if inserted successfuly

d = input()

# Delete entry with key d from my_dict
if d in my_dict:
    del my_dict[d];
    print("Deleted");
else:
    print(-1)
# Print Deleted if deleted successfuly else print -1

p = input()
if p in my_dict:
    print("Marks of "+ p +" is "+ str(my_dict[p]));
else:
    print(-1);

# Print marks of given key p if key present, else print -1
