import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

math_scores = [88, 92, 76, 81, 95, 87, 90, 85, 78, 93]
science_scores = [82, 89, 91, 85, 94, 88, 76, 80, 90, 92]

plt.scatter(math_scores, science_scores, s=100, color='blue', alpha=0.6)
plt.xlabel('Math_Scores') 
plt.ylabel('Science_Scores') 
plt.show()
