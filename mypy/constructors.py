# constructor is a class function with double underscore
# __init__() func gets called wherever an object is created
# we can use it to initialize all variables at the time of object creation

class Employee:

    def __init__(self, name, id):
        self.name = name
        self.id = id

    def printEmpDetails(self):
        print('Emp name: ', self.name)
        print('Emp ID: ', self.id)


emp1 = Employee('John', 1001)
emp2 = Employee('Josh', 1002)

# emp1.printEmpDetails('Elvis', 100)
emp1.printEmpDetails()
# Emp name:  Josh
# Emp ID:  1002
emp2.printEmpDetails()
# Emp name:  Josh
# Emp ID:  1002
