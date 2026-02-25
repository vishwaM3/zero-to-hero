def first_occurrence(arr, target):
    low, high = 0, len(arr) - 1
    ans = -1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            ans = mid
            high = mid - 1   # move left
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return ans
arr=[2,4,4,4,5,6,7,8]
target=4
print(first_occurrence(arr, target))
