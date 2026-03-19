class Subset_num:
    def subsetSums(self, arr):
        # code here
        ans = [0];
        for i in range(len(arr)):
            if arr[i] == False:
                ans.append(arr[i]);
            elif arr[i] == True:
                ans.append(i);
        return ans;
if __name__ == "__main__":
    subset_num = Subset_num();
    print(subset_num.subsetSums([1,2,3,4,5]));