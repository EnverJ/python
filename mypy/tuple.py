print("hello tuple")
#  a tuple is similar to list
# unlike list, elements once assigned to a tuple cannot be changed.
# elements are place inside parenthesis()

my_tuple = ()  # empty
my_tuple2 = (1, 2, 3, 4)  # integers
my_tuple3 = (1, 2, "red", "blue", 3.4)  # mixed
my_tuple4 = (1, 2, ('apple', 'banana'), 3.4)  # nested tuple
my_tuple5 = (1, 2, ['python', 'java'])
print(my_tuple)  # ()
# one item in a tuple
t1 = ('Python')
print(type(t1))  # <class 'str'>
t2 = ('Java',)
print(type(t2))  # <class 'tuple'>

# Accessing tuple elements
t1 = ('a', 'b', 'c', 'd')
print(t1[0])  # a
print(t1[2])  # c

# navigate indexing
print(t1[-1])  # d last item
print(t1[-2])  # c 2nd lst

# selecting to access range of elements
#  slicing elements
my_tuple = ('H', 'e', 'l', 'l', 'o')
print(my_tuple[1:4])  # 2nd to 4th element  # ('e', 'l', 'l')
print(my_tuple[:-3])  # beginning to 2 nd   # ('H', 'e')
print(my_tuple[2:])  # 3rd to end # ('l', 'l', 'o')
print(my_tuple[:])  # all elements # ('H', 'e', 'l', 'l', 'o')
# changing elements of a tuples
# tuple are immutable - elements cannot be changed
# However if tuple contains mutable elements like lists, it can be changed

my_tuple = (1, 2, 3, ['h', 'e', 'l', 'l', 'o'])
print(my_tuple)  # (1, 2, 3, ['h', 'e', 'l', 'l', 'o'])
my_tuple[3][3] = 'o'
print(my_tuple)  # (1, 2, 3, ['h', 'e', 'l', 'o', 'o'])

# + and *
# concatenate tuple using +
# repeat tuple items using *
my_tuple = (1, 2, 3)
print(my_tuple + (4, 5, 6))  # (1, 2, 3, 4, 5, 6)
print(my_tuple * 3)  # (1, 2, 3, 1, 2, 3, 1, 2, 3)

# looping through a tuple
for item in my_tuple:
    print(item)
#     1
# 2
# 3

# deleting a tuple
#  we cannot delete in a tuple
# we can delete the tuple itself
del my_tuple
# print(my_tuple)
