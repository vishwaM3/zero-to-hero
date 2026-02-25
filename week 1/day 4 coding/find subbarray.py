arr=[1,2,3,4]
n=len(arr)
prefix=[0]*n
for i in range(n):
    for j in range(i,n):
        print(arr[i:j+1])