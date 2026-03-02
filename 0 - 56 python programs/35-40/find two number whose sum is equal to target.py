arr=[2,4,5,6,8,3,4,9]
target=11
left=4
right=len(arr)-1
while left<right:
    s=arr[left]+arr[right]
    if s==target:
        print(arr[left],arr[right])
        break
    elif s<target:
        left=left+1
    else:
        right=right-1    