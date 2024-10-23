import matplotlib.pyplot as plt
import numpy as np

flavors = [
    "Vanilla",
    "Chocolate",
    "Strawberry",
    "Mint Chocolate Chip",
    "Cookies and Cream"
]
scoops_sold = np.array([
    120,  # Vanilla
    150,  # Chocolate
    100,  # Strawberry
    80,   # Mint Chocolate Chip
    130   # Cookies and Cream
])
price_per_scoop = np.array([
    5, # Vanilla
    7, # Chocolate
    8, # Strawberry
    4, # Mint Chocolate Chip
    11 # Cookies and Cream
])
colors = ['red','green','blue','black','yellow','magenta']
plt.pie(price_per_scoop*scoops_sold, labels=flavors)
plt.show()

