class Solution:
    def decToBinary(self, n):
        bitarr = [];
        while n > 0:
            rem = n % 2;
            bitarr.append(rem);
            n = n // 2;
        bitarr.reverse();
        return " ".join(map(str,bitarr))
obj = Solution();
print(obj.decToBinary(12));