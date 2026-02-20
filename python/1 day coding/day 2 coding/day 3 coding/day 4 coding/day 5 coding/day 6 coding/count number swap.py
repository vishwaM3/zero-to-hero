arr=[2,1,5,8,9,3,4]
n=len(arr)
count=0
for i in range(n):
    for j in range(0,n-i-1):
        if arr[j]>arr[j+1]:
            arr[j],arr[j+1]=arr[j+1],arr[j]
            count+=1  
print(arr)
print("swap:",count)
