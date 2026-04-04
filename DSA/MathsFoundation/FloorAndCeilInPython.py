import math


# Function to compute and return both
# floor and ceil of a / b
def divFloorCeil(a, b):
    # Compute floor(a / b) using built-in math.floor
    floor_val = math.floor(a / b)

    # Compute ceil(a / b) using built-in math.ceil
    ceil_val = math.ceil(a / b)

    return [floor_val, ceil_val]


if __name__ == "__main__":
    a, b = -7, 2

    res = divFloorCeil(a, b)

    print(res[0], res[1])