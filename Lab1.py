list = [5, 4, 17, 19, 30, 2, 7, 10, 45]
#Q1: Write a Python program to sum all the items in the list.
list_sum = 0
for i in list:
    list_sum +=i
print(list_sum)

#Q2: Write a Python program to get the largest number from the list.
list_sort = list.copy()
list_sort.sort()
print(list_sort[-1])

#Q3: Use list comprehension, create a new list from the above list containing only even numbers.
list_even = [i for i in list if i%2==0]
print(list_even)

#Q4: Use list slicing to get a new list from the previous list starting from the start to the 5th element in the list.
list_slice = list[4:]
print(list_slice)