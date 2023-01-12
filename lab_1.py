from typing import List
# Main list
list1 = [5, 4, 17, 19, 30, 2, 7, 10, 45]

# Sum of numbers
print('sum f items = ', sum(list1))
# Max number
print('largest  number = ', max(list1))

# Even items
even_list = []
for i in range(0, len(list1)):
    if list1[i] % 2 == 0:
        even_list.append(list1[i])
print('even items are ', even_list)

# First 5 items
sub_list = []
for i in range(0, 5):
    sub_list.append(list1[i])
print('list until 5th item ',sub_list)
