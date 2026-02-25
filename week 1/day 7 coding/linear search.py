num=[2,9,6,4,5,3,8]
find=5
found=False
index=0
for i in num:
    if i==find:
        found=True
        print("found at position:",index)
    else:
        index=index+1
if not found:
    print("number is not is found")        