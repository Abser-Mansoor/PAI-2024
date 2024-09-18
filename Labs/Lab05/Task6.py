import abc
from abc import *

class Employee(ABC) :
    def __init__(self, name, salary) :
        self.name = name
        self.salary = salary
    @abstractmethod
    def Bonus() :
        pass

class Manager(Employee) :
    def __init__(self,name,salary) :
        super().__init__(name,salary)
    
    def Bonus(self) :
        return 0.2*self.salary
    
    def hire(self) :
        print(f"{self.name} is hiring someone")

class Developer(Employee) :
    def __init__(self,name,salary) :
        super().__init__(name,salary)
    
    def Bonus(self) :
        return 0.1*self.salary
    
    def writeCode(self) :
        print(f"{self.name} is writing code")

class SeniorManager(Manager) :
    
    def __init__(self, name, salary):
        super().__init__(name, salary)

    def Bonus(self) :
        return 0.3*self.salary
    
manager = Manager("Abser",2000)
developer = Developer("Ali",1000)
Srmanager = SeniorManager("Owais",3000)

manager.hire()
developer.writeCode()

print(f"{developer.name}'s Bonus is {developer.Bonus()}\n{manager.name}'s Bonus is {manager.Bonus()}\n{Srmanager.name}'s Bonus is {Srmanager.Bonus()}")
