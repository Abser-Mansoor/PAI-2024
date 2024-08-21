lis = []

for x in range(3):
    subject = input("Enter name of subject: ")
    lis.append(subject)

marks = {}

for subject in lis:
    marks[subject] = int(input(f"Enter marks for {subject}: "))

average = sum(marks.values()) / len(marks)
percentage = (sum(marks.values()) / 300) * 100

print("Average Marks:", average)
print("Percentage:", percentage)
