import random

otp = ''.join(str(random.randint(0, 9)) for _ in range(4))
print("Generated OTP:", otp)

attempt = 3

while attempt > 0:
    inp = input("Enter OTP :- ")
    if inp == otp:
        print("Welcome Omraje")
        break
    else:
        attempt -= 1
        print(f"Wrong OTP Attempt left {attempt}")

if attempt == 0:
    print("your number is blocked")