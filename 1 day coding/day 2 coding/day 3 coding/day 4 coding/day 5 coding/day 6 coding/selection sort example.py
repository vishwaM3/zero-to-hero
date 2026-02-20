arr=[24,41,33,42,17]
n=len(arr)
for i in range(n-1):
        mini_index=i
        for j in range(i+1,n):
            if arr[j]<arr[mini_index]:
                mini=j
                arr[j],arr[mini_index]=arr[mini_index],arr[j]
print("sorted array:",arr)            