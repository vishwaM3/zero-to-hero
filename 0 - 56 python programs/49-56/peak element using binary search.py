def find_peak(arr):
    low, high = 0, len(arr) - 1

    while low < high:
        mid = (low + high) // 2
        if arr[mid] < arr[mid + 1]:
            low = mid + 1
        else:
            high = mid

    return low   # peak index
arr=[5,7,4,6,3,9,4,7,6,5,1,0] 
print(find_peak(arr))   