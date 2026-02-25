arr=[1,7,5]
n=len(arr)
count=0
for i in range(n):
    mini_index=i
    for j in range(i+1,n):
        if arr[j]<arr[mini_index]:
            mini_index=j
        if mini_index !=i:
            arr[i],arr[mini_index]=arr[mini_index],arr[i]
            count+=1
print("sorted:",arr)
print("swaps:",count)            