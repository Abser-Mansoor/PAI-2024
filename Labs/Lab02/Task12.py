# tanks = ["PzKmpfWg IV", "Jagdpanzer 38(t)", "PzKmpfWg VI Konig Tiger"]
# time = ["1938", "1939", "1942"]

tanks = [item.strip() for item in input("Enter names of tanks seperated by commas: ").split(',')]
times = [item.strip() for item in input("Enter times of their production seperated by commas: ").split(',')]

user_map = {}

for tank,time in zip(tanks,times):
    user_map[tank] = time
    
print(user_map, sep = "\n")
