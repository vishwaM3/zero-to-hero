'''pn= n * (n+ 1)
For example, the first few pronic numbers are:
p1= 1 * (1 + 1) = 2
p2= 2 * (2 + 1) = 6
p3= 3 * (3 + 1) = 12
p4= 4 * (4 + 1) = 20'''

def is_pronic_number(num):
     for n in range(1, int(num**0.5) + 1):
       if n * (n + 1) == num:
          return True
     return False
print("Pronic numbers between 1 and 100 are:")
for i in range(1, 101):
     if is_pronic_number(i):
         print(i, end=" | ")

