try:
    int1 = int(input("Enter first number: "))
    int2 = int(input("Enter second number: "))
    print(int1/int2)
except ZeroDivisionError:
    print("Division by Zero attempted")
except ValueError:
    print("Wrong type of value")
except IOError:
    print("IOError Occured")
except Exception as error:
    print("Unexpected error")
