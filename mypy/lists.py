print("hello!!! lists.py")

# list - store list of items
#  create by putting items inside square brackets []

list1 = []  # empty list
numbers = [2, 3, 4, 5, 6, 7]  # list of integer
color = ['red', 'blue', 'green']  # lists of strings
mixed_list = [1, 2, 3, 4, 'red']  # mixed list
print(mixed_list)  # [1, 2, 3, 4, 'red']

#  a list can have another list as its item
my_list = ['python', 'java', [1, 2, 3], "car"]

# access from a list
numbers = [1, 2, 3, 4, 5]
print(numbers)  # [1, 2, 3, 4, 5]
print(numbers[0])  # 1
# print(numbers[5])  # IndexError: list index out of range
print(numbers[-1])  # 5  last element
print(numbers[-2])  # 4 second last element

# slicing list
print(numbers[2:4])  # [3, 4]
print(numbers[0:5])  # [1, 2, 3, 4, 5]
print(numbers[:-2])  # [1, 2, 3]  # beginning to 3rd
print(numbers[:])  # [1, 2, 3, 4, 5]  # Beginning to end

# lists are mutable - items can be changed
my_colors = ['blue', 'green', 'red', 'white']
print(my_colors)  # ['blue', 'green', 'red', 'white']
my_colors[2] = 'pink'
print(my_colors)  # ['blue', 'green', 'pink', 'white']
my_colors[1:3] = ['orange', 'purple']  # 2nd to 3rd item
print(my_colors)  # ['blue', 'orange', 'purple', 'white']

# add items to a list
numbers = [1, 2, 3, 5]
print(numbers)  # [1, 2, 3, 5]
numbers.append(5)
print(numbers)  # [1, 2, 3, 5, 5]
numbers.extend([6, 7, 8])
print(numbers)  # [1, 2, 3, 5, 5, 6, 7, 8]

print(numbers + [9, 10])  # [1, 2, 3, 5, 5, 6, 7, 8, 9, 10]
# repeat items
print(numbers * 3)  # [1, 2, 3, 5, 5, 6, 7, 8, 1, 2, 3, 5, 5, 6, 7, 8, 1, 2, 3, 5, 5, 6, 7, 8]

# insert items at a desired location insert()
numbers.insert(2, 2.5)
print(numbers)  # [1, 2, 2.5, 3, 5, 5, 6, 7, 8]

# delete items -del
del numbers[2]  # delete the 3rd item
print(numbers)  # [1, 2, 3, 5, 5, 6, 7, 8]
# delete multiple items
del numbers[2: 4]
print(numbers)  # [1, 2, 3, 5, 5, 6, 7, 8]

del numbers
# print(numbers)  # result in error - list not defined

print('---------------------')
numbers = [1, 2, 3, 4, 5]
numbers.remove(1)  # this will remove the first item not the index 1.
print(numbers)  # [2, 3, 4, 5]
numbers.pop(2)  # remove the ite from the index position 2
print(numbers)  # [2, 3, 5]
numbers.pop()  # remove the last item
print(numbers)  # [2, 3]
numbers.clear()  # clear the list
print(numbers)  # []
# Copy list =
list1 = [1, 2, 3]
list2 = list1
print(list2)  # [1, 2, 3]

list1 = [1, 2, 3]
list2 = list1.copy()
print(list2)  # [1, 2, 3]

# loop through a list
fruits = ['apple', 'banana', 'grapes', 'strawberry']
for items in fruits:
    print(items)
# apple
# banana
# grapes
# strawberry


# check item in list
print('apple' in fruits)  # True
print('pear' in fruits)  # False

# nested lists
my_list = [1, 2.0, 3, [1.0, 2.0, 3.0]]
print(my_list)  # [1, 2.0, 3, [1.0, 2.0, 3.0]]
print(my_list[3][1])  # 2.0
