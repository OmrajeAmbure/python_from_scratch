class Subsets:
    def subsets(self, nums):
        ans = []
        def backtrack(index, current):
            if index == len(nums):
                ans.append(current.copy())
                return
            current.append(nums[index])
            backtrack(index + 1, current) # include
            current.pop()
            backtrack(index + 1, current)  # exclude
        backtrack(0,[]);
        return ans;
# Driver code
obj = Subsets()
print(obj.subsets([1, 2, 3]))