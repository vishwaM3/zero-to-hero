arr=(input("enter a number:"))
n=len(arr)
prefix=[0]*len(arr)
prefix[0]=arr[0]
for i in range(1,len(arr)):
    prefix[i]=prefix[i-1]+arr[i]
print(prefix)
for i in range(n):
    for j in range(i,n):
        if i==0:
            print(prefix[j])
        else:
            print(prefix[j]-prefix[i-1 ])        