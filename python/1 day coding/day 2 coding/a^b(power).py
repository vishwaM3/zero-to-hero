def power(a,b):
    if b==0:
        return 1
    else:
        return a*power(a,b-1)
a=int(input("enter a:"))
b=int(input("enter b:"))
print("ans=",power(a,b))
