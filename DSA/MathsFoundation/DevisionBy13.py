def DivisionBy13(s):
    rem = 0;
    for ch in s:
        rem = (rem * 10 + int(ch)) % 13;
    return rem == 0;


def divBy13(s):
    # Convert the string to an integer
    num = int(s)

    # Check if the number is divisible by 13
    return num % 13 == 0
if __name__ == "__main__":
    print(DivisionBy13("2911285"));
    print(divBy13("2911285"));