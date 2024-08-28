def average(temps) :
    avg = 0
    for temp in temps :
        avg += temp
    return avg / len(temps)
    
def extreme(temps) :
    maximum = -float("inf")
    minimum = float("inf")
    for temp in temps :
        if temp > maximum : maximum = temp
        if temp < minimum : minimum = temp
    print("Max: ", maximum, "\nMin: ",minimum)
    
def ascendorder(temps) :
    for index,temp in enumerate(temps) :
        iterator = 0
        for choices in temps :
            if temp > choices : iterator+=1
        temporary = temps[index]
        temps[index] = temps[iterator]
        temps[iterator] = temporary
    return temps
    
def removal(temps,temp) :
    for index,iteration in enumerate(temps) :
        if iteration == temp :
            print("Value at index ", index, " having value ", temps[index], " removed.\n")
            temps.pop(index)
            return
        
print(average([4,6,12,1,10,20,60]))
extreme([4,6,12,1,10,20,60])
print(ascendorder([4,6,12,1,10,20,60]))
removal([4,6,12,1,10,20,60],60)
