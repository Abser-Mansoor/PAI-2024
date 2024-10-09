import numpy as np

h = np.arange(1,19,2).reshape(3,3)
for i in np.nditer(h) :
    print(i)
