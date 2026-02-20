tuple=(1,2,3,4,5)
print(tuple)


# print inner tuple

t=(1,2,3,(4,5,6),7)
t1=t[3]
print(t1)
#print value 5
print(t[3][1])
# length of tuple
print(len(t))


# count numbers
t=(1,7,2,3,3,(4,5,6),7,1)
print(t.count(2),t.count(7))
