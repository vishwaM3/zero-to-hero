def last_occurrence(arr, target):
    low, high = 0, len(arr) - 1
    ans = -1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            ans = mid
            low = mid + 1    # move right
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return ans
arr=[2,4,4,4,5,6,7,8]
target=4
print(last_occurrence(arr, target))
