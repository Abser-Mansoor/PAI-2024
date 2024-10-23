import matplotlib.pyplot as plt

heights = [1,2,3,4,5,6,7,8,9,10,12,11,13,4,15,16,17,18,13,1]
students = [
    "Alice Johnson",
    "Bob Smith",
    "Charlie Brown",
    "Daisy Miller",
    "Ethan Davis",
    "Fiona White",
    "George Black",
    "Hannah Green",
    "Ian Thompson",
    "Julia Wilson",
    "Kevin Lee",
    "Liam Clark",
    "Mia Lewis",
    "Noah Walker",
    "Olivia Hall",
    "Peter Allen",
    "Quinn Young",
    "Rita Adams",
    "Sam Taylor",
    "Tina Harris"
]
colors = ['red','green','blue','black','yellow','magenta']
plt.bar(students,heights,color=colors)
plt.show()
plt.pie(heights,labels=students,colors=colors)
plt.show()
