students = {
    "Abser" : [20,10,20]
}
def addgrade(name, grade):
    if name in students:
        students[name].append(grade)
    else:
        print("Student " + name + " not found.")

def average(name):
    if name in students:
        grades = students[name]
        if grades:
            return sum(grades) / len(grades)
        else:
            print("No grades available for " + name)
    else:
        print("Student " + name + " not found.")

def addstudent(name,grades = []):
    if name not in students:
        students[name] = grades
    else:
        print("Student " + str(name) + " already exists.")

def removestudent(name):
    if name in students:
        del students[name]
        print("Student " + name + " has been removed.")
    else:
        print("Student " + name + " not found.")
    
addgrade("Abser", 100)
print(students)
addstudent("Owais",[100,90,90])
print(students)
print("Average grade of Owais is: " + str(average("Owais")))
addstudent("Owais")
