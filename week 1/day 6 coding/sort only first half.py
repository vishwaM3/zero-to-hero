arr=list(map(int,input("emter a number:").split()))
mid=len(arr)//2
for i in range(mid):
    for j in range(0,mid-i-1):
        if arr[j]>arr[j+1]:
            arr[j],arr[j+1]= arr[j+1],arr[j]
print(arr)            