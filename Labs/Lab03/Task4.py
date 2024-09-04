try:

    name = input("Enter your name: ")
    cnic = input("Enter your cnic number: ")
    age = int(input("Enter your age: "))
    salary = int(input("Enter your salary: "))
    with open(r'text4.txt','w') as fileobj:
         fileobj.write(f"name:{name} CNIC:{cnic} Age:{age} Salary:{salary}")
    contact = input("Enter your contact number")
    with open(r'text4.txt','a') as fileobj:
         fileobj.write(f" Contact:{contact}")
    with open(r'text4.txt','r') as fileobj:
         print(fileobj.read())

except FileNotFoundError:
        print("File not Found")
except IOError:
    print("IOError Occured")
except Exception as error:
    print("Unexpected error")
