s="level"
if s==s[ : :-1]:
    print("palindrome")
else:
    print('not palindrome')    




    #using two pointer
s="level"
i=0
j=len(s)-1
while i<j:
        if s[i]!=s[j]:
            print("not palindrome")
            break
        i+=1
        j-=1
else:
        print("palindrome")    
