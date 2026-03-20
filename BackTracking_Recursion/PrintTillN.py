class Solution:
    def printTillN(self, N):
        if N > 1:
            self.printTillN(N-1);
        print(N,end=" ")
solution  = Solution();
obj1 = solution.printTillN(5);
print()
obj2 = solution.printTillN(10);
print()
print(obj1);
print(obj2);