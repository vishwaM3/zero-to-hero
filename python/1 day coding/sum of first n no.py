def natural(num):
    if num==0:
        return 0
    else:  
        return num+natural(num-1) 


num=int(input("enter a number:"))
print("sum",natural(num))