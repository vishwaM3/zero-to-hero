a=int(input("enter a 1st number;"))
b=int(input("enter a 2st number;"))
c=int(input("enter a 3st number;"))
if a>=b and a>=c:
    print("a is larger",a)
elif b>=a and b>=c:
    print('b is larger',b)
else:
    print("c is larger",c)        