def decrementList(arr):
    for i in range(len(arr)):
        arr[i] = arr[i] - 1;
    return arr;
print(decrementList([54,43,2,1,5]));