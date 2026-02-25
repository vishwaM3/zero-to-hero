s="abc123"
letters=0
digits=0
for i in s:
    if 48<=ord(i)<=57:
        digits+=1
    elif 65<=ord(i)<=90 or 97<=ord(i)<=122:
        letters+=1
print("letters:",letters)
print("digits:",digits)                
