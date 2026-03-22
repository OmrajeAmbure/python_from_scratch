class SubsetSum:
    def subsetSum(self, nums):
        ans = [];
        def solve(index, sum):
            if index == len(nums):
                ans.append(sum);
                return;
            solve(index + 1,sum+nums[index]);
            solve(index + 1, sum);
        solve(0,0);
        return sorted(ans);

obj = SubsetSum();
print(obj.subsetSum([2,3]));
