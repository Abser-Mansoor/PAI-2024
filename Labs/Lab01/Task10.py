lis = []

num = int(input("Enter size of list: "))

for x in range(num):
    lis.append(int(input("Enter a number: ")))
    
print("Max number in list is: ", max(lis))
