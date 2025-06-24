# Manager
# Name, Age, Salary, No of Teams, Location

class Manager:

    def __init__(self,Mname, Mage, Msalary, MNo_of_teams, M_location):
        self.name = Mname
        self.age = Mage
        self.salary = Msalary
        self.teams = MNo_of_teams
        self.location = M_location

    def display(self):
        print(f'Name:{self.name}')
        print(f'Age:{self.age}')
        print(f'Salary:{self.salary}')
        print(f'Teams:{self.teams}')
        print(f'Location:{self.location}')


obj_Manager = Manager('Kalyan',35, 100000, 5, 'Bangalore')
obj_Manager.display()


# Name:Kalyan
# Age:35
# Salary:100000
# Teams:5
# Location:Bangalore