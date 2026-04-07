def powMod(x, n, M):
    res = 1

    # loop from 1 to n
    for _ in range(n):
        # Multiplying res with x
        # and taking modulo to avoid overflow
        res = (res * x) % M
    return res


if __name__ == "__main__":
    x, n, M = 3, 2, 4
    print(powMod(x, n, M))