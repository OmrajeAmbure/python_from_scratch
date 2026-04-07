class Solution:
    def closestNumber(self, n, m):
        if n % m == 0:
            return n
        lower = (n // m) * m
        upper = lower + m
        print(abs(lower));
        print(abs(upper));
        if abs(n - lower) < abs(n - upper):
            return lower
        else:
            return upper

if __name__=="__main__":
    s = Solution();
    print(s.closestNumber(13,4));