# if ... else statement
# if boolean_exp:
# statement
age = 100
if age >= 18:
    print("eligible for DL")
else:
    print("not eligible to DL")
print("outside of if")

#  elif
# if you have more than two options to choose from
num = 10
if num > 0:
    print("number is positive")
elif num < 0:
    print("number is negative")
else:
    print("number is zero")

#  nested if .. else
#  one if ... else statement inside another
num = float(input("Enter a number\n"))
if num >= 0:
    if num == 0:
        print("zero")
    else:
        print("positive")
else:
    print("number is negative")
