#
# # while loop
# while boolean_exp:
#     statement

a = 9
b = 1
while b <= a:
    print("I am inside the while loop")
    b += 1
# I am inside the while loop
# I am inside the while loop
# I am inside the while loop
# I am inside the while loop
# I am inside the while loop
# I am inside the while loop
# I am inside the while loop
# I am inside the while loop
# I am inside the while loop

#  some natural numbers
n = 10
sum1 = 0
i = 1
while i <= n:
    sum1 = sum1 + i
    i += 1
print("sum is :", sum1)
#    sum is : 55


# while loop can have optional else block. else is executed when cond in while is false

i = 0
while i <= 3:
    print("I am inside the loop")
    i = i + 1
else:
    print("I am inside the else")
#     I am inside the loop
# I am inside the loop
# I am inside the loop
# I am inside the loop
# I am inside the else

#  for loop
number = range(1, 11)
#  range in python is used to create sequence of number
sum1 = 0
for i in number:
    sum1 = sum1 + i
print("sum is: ", sum1)  # sum is:  55

#  for with else
number = range(1, 4)
for i in number:
    print("inside for loop")
else:
    print("print inside else")
#     inside for loop
# inside for loop
# inside for loop
# print inside else

my_list = [1, 2, 3, 4]
for item in my_list:
    print(item)
else:
    print("item is completed")
# 1
# 2
# 3
# 4
# item is completed

# break
#  break and continue statement can alter thr fow of the normal flow
numbers = [1, 2, 3, -3, 0, 7, 10]
for i in numbers:
    if i < 0:
        print("value is negative")
        break
    print(i)
#     1
# 2
# 3
# value is negative

#  continue used to skip the current iteration of the loop
i = 1
while i <= 5:
    print("value of i is: ", i)
    i += 1
    if i == 3:
        print("i is 3")
        continue
# value of i is:  1
# value of i is:  2
# i is 3
# value of i is:  3
# value of i is:  4
# value of i is:  5
print("---------")
num = [1, 2, 3, 4, -2, 5, 7]
for val in num:
    if val < 0:
        print("negative value")
        continue
    print(val)
# 1
# 2
# 3
# 4
# negative value
# 5
# 7

#  pass
#  any loop or any fun that is not yet implemented
for n in [1, 2, 3, 4]:
    pass
