s="vishwa"
rev=""
for i in s:
    rev=i+rev
print(rev)    


# reverse a string using two pointer
s="ambika"
i=0
j=len(s)-1
s=list(s)
while i<j:
    s[i],s[j]=s[j],s[i]
    i+=1
    j-=1
print("".join(s))



# reverse using slicing
s="vishmbika"
print(s[::-1])
