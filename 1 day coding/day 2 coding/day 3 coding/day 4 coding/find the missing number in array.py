def num_missing_sort(arr):
    arr.sort()
    for i in range(len(arr)):
        if arr[i]!=i+1:
            return i+1
    return len(arr)+1
#example
arr=[1,2,4,5,6]
print("missing num:",num_missing_sort(arr))            