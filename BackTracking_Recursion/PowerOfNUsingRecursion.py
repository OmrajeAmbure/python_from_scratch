class PowerProblem:
    def __init__(self):
        pass
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0:
            return False
        if n == 1:
            return True
        if n % 2 != 0:
            return False
        return self.isPowerOfTwo(n // 2);
    def isPowerOfThree(self, n: int) -> bool:
        if n == 0 : return False;
        if n == 1 : return True;
        if n%3 != 0 : return False;
        return self.isPowerOfThree(n//3);
    def isPowerOfFour(self, n: int) -> bool:
        if n == 0 : return False;
        if n == 1 : return True;
        if n%4 != 0 : return False;
        return self.isPowerOfFour(n//4);
power2ans = PowerProblem();
for i in range(1,100):
    print(f"Num {i} for the isPowerOfTwo : {power2ans.isPowerOfThree(i)}")
