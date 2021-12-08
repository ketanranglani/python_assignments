student = []
 
# number of elements as input
n = 6
 
# iterating till the range
for i in range(0, n):
    ele = int(input())
 
    student.append(ele) # adding the element
     
student.sort()
print(student)