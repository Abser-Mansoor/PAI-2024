lis = list(range(51))

for x in lis:
    if x % 3 == 0 and x % 5 == 0: print("fizzbuzz")
    elif x % 3 == 0: print("fizz")
    elif x % 5 == 0: print("buzz")
    else: print (x)
