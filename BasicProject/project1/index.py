import random

random.seed(12) # Random numbers depend on the seeding value . The seed makes these numbers the same every time we run the code with a seed of n.

print(random.randint(1,100000)) # random.randint() method is used to generate random integers between the given range
print(random.randint(-100,-1))
print(random.random()) #  A random.random() method is used to generate random floats between 0.0 to 1.


#  Randomly Select from List, String, and Tuple
a = [1, 2, 3, 4, 5, 6]
print(random.choice(a))

s = "geeks"
print(random.choice(s))

tup = (1, 2, 3, 4, 5)
print(random.choice(tup))

# Select Multiple Unique Random Items

otp = random.sample(range(1, 10), 4)
print(otp)
inp = input()
inp = list(inp.split(','))
inp = [int(x) for x in inp]
if otp == inp:
    print("Welcome om ")
else:
    print("Worong OTP plese try again...")
