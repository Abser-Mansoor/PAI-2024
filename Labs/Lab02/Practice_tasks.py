# Task 1
def print_greeting() : 
  return "Hello"

print(print_greeting())

# Task 2
def rectarea(length,breadth) :
    return length*breadth

print(rectarea(4,6))

# Task 3
def maxnum(*nums):
  maxvalue = -float("inf")
  for num in nums :
      if (num > maxvalue) : maxvalue = num
  return maxvalue

print(maxnum(1,2,3,4,6))

# Task 4
def show_info(**details) :
    print("Details: ", details, sep = "\n")

show_info(name = "Abser", Age = "18", Employed = "True")

# Task 5
response = (input("your good name!\n"))

print("Hello ", response)
response = (input("I hope you are fine, let me know how I can help you\n"))

if (response == "yes") :
    response = (input("Share your problem with us\n"))
    print("Thanks for your feedback, we will resolve your problem")
else : 
    print("Okay! Good to see you , stay connected".center(10))
