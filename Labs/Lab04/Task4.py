class Employee :
    def __init__(self, name, salary, tax) :
        self.name = name
        self.salary = salary
        self.tax = tax
    def Salary_After_Tax(self) :
        self.salary = self.salary - self.salary*(self.tax/100)
        return self.salary
    def Update_Tax_Percentage(self, tax) :
        self.tax = tax

emp = Employee("Abser",2000,2)
print(emp.Salary_After_Tax())
emp.Update_Tax_Percentage(3)
print(emp.Salary_After_Tax())
