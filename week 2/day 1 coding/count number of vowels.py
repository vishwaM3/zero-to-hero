s=input("enter a name or string:")
count=0
for i in s:
    if i in "aeiouAEIOU":
        count+=1
print(count)        