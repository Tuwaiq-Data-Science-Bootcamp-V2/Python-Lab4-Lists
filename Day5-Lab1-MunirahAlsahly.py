# Create the list:
original_list = [5, 4, 17, 19, 30, 2, 7, 10, 45]
print()
print("The given list is:   ",original_list)


# Create function to sum all items in the list:
def sum_all_items(lst):
    sum = 0
    for element in lst:
        sum+=element
    print("--------------------------------------- ")  
    print("The Sum of all items in the list: ",sum)
    print("--------------------------------------- ")
sum_all_items(original_list)

# Print the largest element in the list using max function:
print("The largest item in the list: ", max(original_list))
print("--------------------------------------- ") 

# Create new list using list comprehension
new_list = [m for m in original_list if m%2==0]
print("Create new list using  list comprehension\nThe NEW LIST is: ",new_list )
print("--------------------------------------- ")

# Get the first 5 elements in the second_list (in this case it is all elements) 
print("Create new list using  slicing\nThe FIRST 5 ITEMS in the list are: ",new_list[:4]) #5th element is in index 4 in the list range
print("--------------------------------------- ")
print()