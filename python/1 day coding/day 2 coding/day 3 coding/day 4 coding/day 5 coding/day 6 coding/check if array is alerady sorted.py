def sorted(arr):
    n=len(arr)
    for i in range(n-1):
        if arr[i]>arr[i+1]:
            return False
    return True
print(sorted([5,6,7,6,3,2,1]))            
