import matplotlib.pyplot as plt

populations = [
    37.4,  # Tokyo
    31.0,  # Delhi
    24.1,  # Shanghai
    21.6,  # Mexico City
    20.5,  # Cairo
    20.4   # Mumbai
]
cities = [
    "Tokyo",
    "Delhi",
    "Shanghai",
    "Mexico City",
    "Cairo",
    "Mumbai"
]
colors = ['red','green','blue','black','yellow','magenta']
plt.bar(cities,populations)
plt.ylabel('In Millions')
plt.show()

