def BinaryConversion(n) -> str:
    if n == 0 or n==1:
        return "".join(n);
    binArr = []
    while n > 0:
        bit = n % 2
        binArr.append(str(bit))
        n //= 2

    # reverse the string
    binArr.reverse()
    return "".join(binArr)
def BinaryConversionBitwiseOperator(n)->str:
    bin = ""
    while n>0:
        bit = (n & 1);
        bin += str(bit);
        n = n >> 1
    return bin[::-1];
if __name__=="__main__":
    print(BinaryConversion(12))
    print(BinaryConversionBitwiseOperator(4))
