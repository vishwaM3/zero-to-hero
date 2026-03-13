num=[1,2,3,4,5,6]
list=[x for x in num]
print(list)    

#nested list
nested_list=[[1,2,3],[1,2,3],[1,2,3]]
comprehension=[[i for i in range(1,4)]for j in range(3)]
print(comprehension)
  
  
  #print row 

nested=[[1,2,3],[4,5,6],[7,8,9]]
[print(row) for row in nested]


# create sub list
nums=[1,2,3,4,5,6,7,8,9]
nested=[nums[i:i+2] for i in range(0,len(nums),2)]
print(nested)

#floting numbers to integer numbers
num=[1.2,3.9,5.6]
l=[int(x) for x in num]
print(l)
