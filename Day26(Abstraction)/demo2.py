from abc import ABC, abstractmethod


class Abs_Practice(ABC):

    @abstractmethod
    def login_time(self):
        pass

    @abstractmethod
    def logout_time(self):
        pass


# obj_Abs = Abs_Practice()
# obj_Abs.login_time()
# TypeError: Can't instantiate abstract class Abs_Practice without an implementation for abstract methods 'login_time', 'logout_time'


class TCS(Abs_Practice):

    def login_time(self):
        print('Login time is 9AM')

    def logout_time(self):
        print('Logout time is 6PM')


obj_TCS = TCS()
obj_TCS.login_time()
# obj_TCS.logout_time()

# Login time is 9AM
# Logout time is 6PM


