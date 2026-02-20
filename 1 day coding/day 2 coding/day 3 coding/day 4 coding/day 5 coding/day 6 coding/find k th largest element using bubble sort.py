arr=list(map(int,input("enter nums:").split()))
n=len(arr)
k=4
for i in range(k):
    for j in range(0,n-i-1):
        if arr[j]< arr[j+1]:
         arr[j],arr[j+1]=arr[j+1],arr[j]
print(arr[n-k])            
