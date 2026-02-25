arr=[2,3,5,9,7]
left=0
seen=set()
max_len=0
for right in range (len(arr)):
    while arr[right]in seen:
        seen.remove(arr[left])
        left+=1
    seen.add(arr[right]) 
    max_len=max(max_len,right-left+1)
print(max_len)       