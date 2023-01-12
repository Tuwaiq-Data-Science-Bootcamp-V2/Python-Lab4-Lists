#!/usr/bin/env python
# coding: utf-8

# #### Q1: Write a Python program to sum all the items in the list.

# In[7]:


my_list = [5, 4, 17, 19, 30, 2, 7, 10, 45]


total = 0

for num in my_list:
    total += num

print(total)


# #### Q2: Write a Python program to get the largest number from the list.

# In[8]:


#largest number in a list
my_list1 = [5, 4, 17, 19, 30, 2, 7, 10, 45]

# sorting the list
my_list.sort()
 
# printing the last element
print("Largest element is:", my_list[-1])


# #### Q3: Use list comprehension, create a new list from the above list containing only even numbers.

# In[21]:



new_list2=[x for x in my_list if x % 2== 0]
new_list2


# #### Q4: Use list slicing to get a new list from the previous list starting from the start to the 5th element in the list.

# In[12]:


my_list2 = [5, 4, 17, 19, 30, 2, 7, 10, 45]

[x for x in my_list2[0:5]]

