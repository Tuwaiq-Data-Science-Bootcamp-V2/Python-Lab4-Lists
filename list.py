L = [5, 4, 17, 19, 30, 2, 7, 10, 45]


print(L)

# Q1: Write a Python program to sum all the items in the list.
# Answer
listsum = 0
for item in L:
    listsum+=item

print(f"Q1 sum all the items: {listsum}")


#Q2: Write a Python program to get the largest number from the list.
# Answer
Max = 0
for item in L:
    if(item>Max):
        Max = item

print(f"Q2 largest number in the list: {Max}")

#Q3: Use list comprehension, create a new list from the above list containing only even numbers.
# Answer
evenList= [item for item in L if item%2==0]

print(f"Q3 list containing only even numbers: {evenList}")


#Q4: Use list slicing to get a new list from the previous list starting from the start to the 5th element in the list.
# Answer
newList = L[:5]

print(f"Q4 list starting from the start to the 5th element in the list: {newList}")