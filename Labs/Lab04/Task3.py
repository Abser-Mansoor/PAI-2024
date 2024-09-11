class Student:
    def __init__(self,name,age) :
        self.name = name
        self.age = age

    def biodata_print(self) :
        print(f"Name is {self.name}\nAge is {self.age}")

student = Student("Abser",18)
student.biodata_print()
