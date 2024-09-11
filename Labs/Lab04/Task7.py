class Vehicle :
    def __init__(self, capacity) :
        self.capacity = capacity
        self.fare = capacity*100
    
    def print_fare(self) :
        print(f"Fare for the Vehicle is {self.fare}")

class Bus(Vehicle) :
    def __init__(self,capacity):
        super().__init__(capacity)
        self.fare *= 1.1

bus = Bus(100)
bus.print_fare()
