# Binary exponentiation
def power(base, exp, mod):
    result = 1
    base %= mod
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        base = (base * base) % mod
        exp //= 2
    return result


# function to calculate GCD
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def modInverse(b, m):
    return power(b, m - 2, m)


def modDivide(a, b, m):
    # Division not possible
    if b == 0 or gcd(b, m) != 1:
        return -1
    inv = modInverse(b, m)
    return (a * inv) % m


if __name__ == "__main__":
    a, b, m = 10, 2, 13
print(modDivide(a, b, m))