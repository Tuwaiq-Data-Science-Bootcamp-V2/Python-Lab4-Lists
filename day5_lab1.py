list1 = [5,4,17,19,30,2,7,10,45]

#Q1
sum = 0
for i in list1:
    sum += i
print(sum)

#Q2
largestnum =0
for i in list1:
    if i > largestnum:
        largestnum = i

print(largestnum)


#Q3
list2 = [ item for item in list1 if item % 2 != 0 ]
print(list2)

#Q4

print(list1[0:5])

    

