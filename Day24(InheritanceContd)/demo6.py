# Employee : Name, Age, salary, location, technology

class Employee:

    def __init__(self, Ename, Eage, Esalary, Elocation, Etechnology):
        self.name = Ename
        self.age = Eage
        self.salary = Esalary
        self.location = Elocation
        self.technology = Etechnology


    def display(self):
        print(f'Name:{self.name}\n Age:{self.age}\n Salary:{self.salary}\n Location:{self.location}\nTechnology:{self.technology}')


obj_Employee = Employee('Jasmine',25, 30000, 'Delhi','Python')
obj_Employee.display()

# Name:Jasmine
#  Age:25
#  Salary:30000
#  Location:Delhi
# Technology:Python
