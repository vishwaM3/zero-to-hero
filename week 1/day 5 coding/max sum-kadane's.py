arr=[ -1,4,6,-2,5,8,-2,1]
current_sum=0
max_sum=arr[0]
for num in arr:
    current_sum+=num
    max_sum=max(max_sum,current_sum)
    if current_sum<0:
        current_sum=0
print(max_sum)        