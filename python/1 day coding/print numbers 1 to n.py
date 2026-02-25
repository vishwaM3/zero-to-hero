def show(n):
    if n==0:
        return 
    show(n - 1)
    print(n)
    

n=int(input("enter a value:"))
show(n)