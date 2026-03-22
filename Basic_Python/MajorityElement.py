class Solution:
    def majorityElement(self, arr):
        n = len(arr)

        for i in range(n):
            count = 0  # reset for each element

            for j in range(n):  # check entire array
                if arr[i] == arr[j]:
                    count += 1

            if count > n // 2:
                return arr[i]

        return -1

# Driver
obj = Solution()
print(obj.majorityElement([1, 2, 3, 2, 2, 2, 2, 3, 1, 4, 5, 6, 7, 8, 9]))
print(obj.majorityElement([1, 9]))
print(obj.majorityElement([2]))