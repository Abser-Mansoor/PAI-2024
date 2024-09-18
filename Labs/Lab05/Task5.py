import abc
from abc import *

class Vehicle(ABC) :
    def __init__(self,make,model,rental,status) :
        self.make = make
        self.model = model
        self.__rental_price = rental
        self.availability_status = status
    def check_availability(self) :
        print("Vehicle is Available") if self.availability_status else print("Vehicle is not available")

    def calculate_rent(self,time) :
        return self.__rental_price * time
    
    def rent(self) :
        self.availability_status = False

    def returning(self) :
        self.availability_status = True
    @abstractmethod
    def display_details(self) :
        pass
    
    def get_price(self) :
        return self.__rental_price

class SUV(Vehicle) :
    def __init__(self,make,model,rental,status) :
        super().__init__(make,model,rental,status)

    def display_details(self):
        print(f"SUV make is {self.make}\nSUV model is {self.model}\nSUV rent is {self.get_price()}\nSUV availability is {self.availability_status}")

class Truck(Vehicle) :
    def __init__(self,make,model,rental,status) :
        super().__init__(make,model,rental,status)

    def display_details(self):
        print(f"Truck make is {self.make}\nTruck model is {self.model}\nTruck rent is {self.get_price()}\nTruck availability is {self.availability_status}")

class Car(Vehicle) :
    def __init__(self,make,model,rental,status) :
        super().__init__(make,model,rental,status)

    def display_details(self):
        print(f"Car make is {self.make}\nCar model is {self.model}\nCar rent is {self.get_price()}\nCar availability is {self.availability_status}")

class RentalReservations :
    def __init__(self,vehicle,start,end) :
        self.vehicle = vehicle
        self.start = start
        self.end = end
    
    def display_details(self) :
        print(f"Vehicle details are {self.vehicle.display_details()}\nRent price is {abs(self.vehicle.calculate_rent(self.start-self.end))}\nRent starts at {self.start} and ends at {self.end}")

class Customer :
    def __init__(self,name,contact,vehicles) :
        self.__name = name
        self.__contact = contact
        self.__vehicles_rented = vehicles

    def rent(self,rentable) :
        self.__vehicles_rented.append(rentable.vehicle.make)
        rentable.vehicle.rent()
        rentable.display_details()

    def display_details(self) :
        print(f"Customer name is {self.__name}\nCustomer contact number is {self.__contact}\nVehicles rented are {self.__vehicles_rented}")

abser = Customer("Abser", "002222111", ["Corolla", "Bobcat", "Rover"])
rentable_1 = RentalReservations(Car("Car","Honda 1999",50,True),8,12)
rentable_2 = RentalReservations(Truck("Truck","Toyota 2001",80,True),8,12)
rentable_3 = RentalReservations(SUV("SUV","Hyundai 2000",100,True),8,12) #assuming 24 hour clock is used without any decimals
abser.rent(rentable_1)
abser.rent(rentable_2)
abser.rent(rentable_3)
abser.display_details()
