print("first line \n\n")
print("second line")

"""name = input("Enter a name \n\n")
print(name)
print(type(name))"""

# variable
a = 10
b = 2.8989
a = 3
first_name = "Enver"
print(a)

# Literals
# numeric, string, boolean
10, 0, -10
name = "python"
char = 'P'
a = True
b = False

# String
name = "Kudret"
char = 'A'
multiline_string = """
name : Ezmet
subject: Python
job: Teacher
"""
print(multiline_string)

# Type conversion
# implicit
# explicit

num_int = 5
print(type(num_int))
num_float = 5.5
sum = num_int + num_float
print(sum)
print(type(sum))

# explicit
# int()
# float()
# str
a = '77'
int_num = int(a)
print(int_num)
print(type(int_num))

float_num = float(a)
print(float_num)
print(type(float_num))

# Operators
#  are symbols that carry out arithmetical or logical operation

a = 5
b = 10
sum = a + b
print(sum)
result = 8 * 9
print(result)

# * can also be used to repeat string
a = 'python'
b = a * 3
print(b)  # pythonpythonpython

"""a = 'abc'
b = a * '3'
print(b)"""  # TypeError: can't multiply sequence by non-int of type 'str'

result = 17 / 2
print(result)  # 8.5
result = 17 // 2
print(result)  # 8

result = 17 % 2
print(result)  # 1
# ** operator
# left operand is raised to the power of the right operand
result = 2 ** 3
print(result)  # 8
# in python , we can assign multiple values to multiple variables at once
a, b, c = 2, 3, 4
print(a, b, c)  # 2 3 4
x = y = z = "python"
print(x, y, z)  # python python python

# OPerator precendence
print(10 - 3 + 2 * 3)

import booleanExpression
