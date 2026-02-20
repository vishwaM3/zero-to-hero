arr=[2,4,3,6,8]
n=len(arr)
for i in range(n):
    total=0
    for j in range(1,n):
        total+=arr[j]
        print(f"subarray {arr[i:j+1]} -> sum={total}")