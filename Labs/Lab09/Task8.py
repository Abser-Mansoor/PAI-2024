import numpy as np
import abc as ab
import seaborn as sb
import pandas as pd
import matplotlib.pyplot as plt

# Separate dataset and age groups used to accomodate that dataset as the specified dataset was not provided

x = [2000,2001,2002,2003,2004,2005,2006,2007,2008,2009]
y1 = [4,6,11,19,30,45,46,50,53,58]
y2 = [80,78,71,66,56,54,44,43,36,31]

plt.plot(x,y1,color='blue',marker='s',label='Python')
plt.plot(x,y2,color='blue',marker='o',label='CPP')
plt.xlabel('First Decade Of The 21st Century')
plt.ylabel('Positive Reception')
plt.title('Comparing Positive Reception of Python and CPP')
plt.legend(loc='lower right')
plt.show()
