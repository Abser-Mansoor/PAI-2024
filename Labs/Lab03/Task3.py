try:
    # tanks = ["PzKmpfWg IV", "Jagdpanzer 38(t)", "PzKmpfWg VI Konig Tiger"]
    # times = ["1938", "1939", "1942"]    
    plane = [item.strip() for item in input("Enter names of aircraft separated by commas ").split(',')]
    times = [item.strip() for item in input("Enter times at which production started: ").split(',')]
    
    dictionary = {}

    for time,planes in zip(times,plane):
        dictionary[planes] = time

    with open(r'text3.txt','w') as fileobj:
        fileobj.write(str(dictionary))
except FileNotFoundError:
    print("File not Found")
except IOError:
    print("IOError occured")
except Exception as error:
    print("Unexpected Error Occured") 
