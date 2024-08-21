marks = {
    "Physics": int(input("Enter marks for Physics: ")),
    "Chemistry": int(input("Enter marks for Chemistry: ")),
    "Maths": int(input("Enter marks for Maths: "))
}

average = sum(marks.values()) / len(marks)

highest = max(marks, key=marks.get)

print("Average Marks:", average)
print(f"Highest Marks in {highest}: {marks[highest]}")
