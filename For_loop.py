mixed_list = [2,"hello",22.1,445,True]

for element in mixed_list:
    print(element)


sum=0
for i in range(0,31):
    sum=sum+i

print(sum)


sum1=0
for i in range(1,31,2):
    sum1=i+sum1
print(sum1)

number =[1,3,2,3,2,4]
#for i in range(len(number)-1,0,-1):
 #   print(i)

for i in number[::-1]:
     print(i)