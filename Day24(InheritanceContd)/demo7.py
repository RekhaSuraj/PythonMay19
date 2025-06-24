# Manager : Name, Age, Salary, No of Teams, Location

# Employee : Name, Age, salary, location, technology

# common: Name, Age, salary, location

class Profile:

    def __init__(self, Name, Age, Salary, Location):
        self.name = Name
        self.age = Age
        self.salary = Salary
        self.location = Location


class Manager(Profile):

    def __init__(self, Name, Age, Salary, Location, No_of_Teams):
        super().__init__(Name,Age,Salary,Location)
        self.no_of_teams = No_of_Teams


    def display(self):
        print(f'Name:{self.name}')
        print(f'Age:{self.age}')
        print(f'Salary:{self.salary}')
        print(f'Teams:{self.no_of_teams}')
        print(f'Location:{self.location}')


class Employee(Profile):

    def __init__(self, Name, Age, Salary, Location, Technology):
        Profile.__init__(self, Name, Age, Salary,Location)
        self.technology = Technology



    def show(self):
        print(
            f'Name:{self.name}\n Age:{self.age}\n Salary:{self.salary}\n Location:{self.location}\nTechnology:{self.technology}')



obj_Manager = Manager('Amar',35, 200000, "AP",10)
obj_Manager.display()

print()

obj_Employee = Employee('Rita',25, 50000, 'Bidar','Java')
obj_Employee.show()

# Name:Amar
# Age:35
# Salary:200000
# Teams:10
# Location:AP
#
# Name:Rita
#  Age:25
#  Salary:50000
#  Location:Bidar
# Technology:Java


