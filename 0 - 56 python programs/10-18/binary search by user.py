a=[10,20,60,80,42,66,34]
num=int(input("enter a number:"))
a.sort()
low=0
high=len(a)-1
found=False
while low<=high:
    mid=(low+high)//2
    if a[mid]==num:
        found=True
        break
    elif a[mid]<num:
        low=mid+1
    else:
        high=mid-1


if found:
    print("found")
else:
    print("not found")    
