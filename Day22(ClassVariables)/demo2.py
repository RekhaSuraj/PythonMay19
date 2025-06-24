# Update class variables
class Employee:
    company = 'HAL'

    def __init__(self, Name, idNum):
        self.name = Name
        self.idNumber = idNum


    def display(self):
        print(f'Name:{self.name}')
        print(f'ID Number:{self.idNumber}')
        print(f'Company:{self.company}')


    def update_class_var(self, new_name):
        Employee.company = new_name


    def delete_class_var(self):
        del Employee.company

ob1 = Employee('John',1234)
ob1.display()
print()
ob1.update_class_var("TCS")
ob1.display()

# Name:John
# ID Number:1234
# Company:HAL
#
# Name:John
# ID Number:1234
# Company:TCS


ob1.delete_class_var()
ob1.display()

# AttributeError: 'Employee' object has no attribute 'company'