def employee(name: str, salary = 10000) :
    print("Name: ",name)
    salary = salary - salary*0.02
    print("Salary After Tax: ", salary)

employee("Abser",5000)
employee("Fasih")
