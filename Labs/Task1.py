import abc
from abc import *

class Vehicle(ABC) :
    def __init__(self, cap) :
        self.capacity = cap
        self.fare = self.capacity*100
    @abstractmethod
    def calculate(self) :
        pass

class Bus(Vehicle) :
    def __init__(self,cap) :
        super().__init__(cap)
    def calculate(self) :
        self.fare = 1.10*self.fare


bus = Bus(100)
bus.calculate()
print(f"Bus has Seating capacity of {bus.capacity} and fare {bus.fare}")
