students = 
{
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

def addstudent(name):
    if name not in students:
        students[name] = []
    else:
        print(f"Student {student_name} already exists.")

def removestudent(name):
    name in students:
        del students[name]
        print("Student " + name + " has been removed.")
    else:
        print("Student " + name + " not found.")
    
def main() : 
    addgrade("Abser", [10])
    addstudent("Owais",[100,90,90])
    average("Owais")
