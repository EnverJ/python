print("Hello Function!!!")


#  a block of code which runs only when called
#  we can pass data to a func - parameters
# func can return data as result

# def func_name(parameters):
#     statement


def hello(name):
    print("hello", name)


hello("ezmet")
hello("Kudret")


#  funcs to add 2 numbers
def add(num1, num2):
    return num1 + num2


print(add(2, 4))
print(add(3, 5))

# Build-in functions
# print(), input(), range()

# variables
x = 10


def my_func():
    x = 5
    print("value od x inside dunc is : ", x)


my_func()
print("value of x outside func is: ", x)


# Arguments (parameters)
def hello(name, msg='Hpw are you'):
    print("hello", name + ',' + msg)


hello('python', 'Good morning')  # hello python,Good morning
# default value
hello('python')  # hello python,Hpw are you


# positional arguments
def hello(name, msg):
    print("hello", name + ',' + msg)


hello("Eric", "Good evening")  # hello Eric,Good evening
hello(msg="How are you", name="Elvisl")  # hello Elvisl,How are you


# Arbitrary arguments
# when we are not sure about the sum of arguments
def hello(*names):
    print("hello", names)


hello("Eric", "Monil", "Dinesh")  # hello ('Eric', 'Monil', 'Dinesh')

# Anonymous func | Lambda functions
# we can define a func without a name
# labmda arguments: expression
sum = lambda a, b, c: a + b + c
print(sum(2, 3, 4))  # 9


# Recursive functions
# a func can call other fnc and also itself
# a func that calls itself - recursive
# process - recursion


# program to find sum of natural numbers
# 1+2+3
def calculate_sum(n):
    if n == 1:
        return 1
    else:
        return n + calculate_sum(n - 1)


sum = calculate_sum(10)
print(sum) # 55
