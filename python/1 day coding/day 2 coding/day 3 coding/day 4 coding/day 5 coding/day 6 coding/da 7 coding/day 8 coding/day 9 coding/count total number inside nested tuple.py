t=(1,2,(3,8,9),3,(2,4,5,6,7))
count=0
for i in t:
    if type(i)==tuple:
        count+=len(i)
    else:
        count+=1
print(count)            