numbers=[22,44,66,77,22,99,65,44]
numbers.sort()
find=65
found=False
low=0
high=len(numbers)-1
while low<=high:
    mid=high+low//2
    if numbers[mid]==find:
        print('found at',mid)
        found=True
        break
    if numbers[mid]>find:
        high=mid-1
    else:
        low=mid+1
if not found:
     print('not found')           