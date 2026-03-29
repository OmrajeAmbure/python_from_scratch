def extendAP(arr):
    if len(arr)  < 2:
        return tuple(arr);
    n = len(arr);
    differance = arr[n-1] - arr[n-2];
    ans = [];
    for i in range(len(arr)):
            ans.append(arr[i]);
    for i in range(3):
            ans.append(ans[len(ans)-1] + differance)
    return  tuple(ans);
print(extendAP((1,5,9,13,17)));
print(extendAP((3,1,-1,-3,-5,-7)));
print(extendAP((3,)));
