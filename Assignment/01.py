class Animal:
    def __init__(self, name, age, habitat):
        self.name = name
        self.age = age
        self.habitat = habitat
        # Initially, all animals are available for viewing
        self.available_for_viewing = True

    def setAvailability(self, available):
        self.available_for_viewing = available

    def display(self):
        print(
            f"Name: {self.name}, Age: {self.age}, Habitat: {self.habitat}, Available: {self.available_for_viewing}")


class Mammal(Animal):
    def __init__(self, name, age, habitat, fur_length, diet_type):
        super().__init__(name, age, habitat)
        self.fur_length = fur_length
        self.diet_type = diet_type

    def display(self):
        super().display()
        print(
            f"Fur Length: {self.fur_length}, Diet Type: {self.diet_type}\n")


class Bird(Animal):
    def __init__(self, name, age, habitat, wingspan, flight_altitude):
        super().__init__(name, age, habitat)
        self.wingspan = wingspan
        self.flight_altitude = flight_altitude

    def display(self):
        super().display()
        print(
            f"Wingspan: {self.wingspan}, Flight Altitude: {self.flight_altitude}\n")


class Reptile(Animal):
    def __init__(self, name, age, habitat, scale_pattern, venomous):
        super().__init__(name, age, habitat)
        self.scale_pattern = scale_pattern
        self.venomous = venomous  # True is venomous, False is non-venomous

    def display(self):
        venom_status = "Venomous" if self.venomous else "Non-Venomous"
        super().display()
        print(
            f"Scale Pattern: {self.scale_pattern}, Venomous: {venom_status}\n")


lion = Mammal("Lion", 5, "Savannah", "Short", "Carnivore")
parrot = Bird("Parrot", 2, "Rainforest", "25 cm", "High")
snake = Reptile("Python", 3, "Swamp", "Spotted", False)

lion.display()
parrot.display()
snake.display()

lion.setAvailability(False)
parrot.setAvailability(True)
snake.setAvailability(False)

print("\nAfter updating availability:\n")
lion.display()
parrot.display()
snake.display()

print("\nAfter updating availability:\n")
print(lion.display_info())
print(parrot.display_info())
print(snake.display_info())
