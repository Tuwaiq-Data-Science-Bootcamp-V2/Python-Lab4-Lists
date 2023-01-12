#-------- Q1 --------

list1 = [5,4,17,19,30,2,7,10,45]
result =0
for x in list1:
    result +=x
print(result)


#---------- Q2----------

list1.sort()
print(list1[-1])


#-------- Q3 -------

new_list = [x for x in list1 if x%2==0]
print(new_list)


#-------- Q4 ------

list2 = list1[:5]
print(list2)
