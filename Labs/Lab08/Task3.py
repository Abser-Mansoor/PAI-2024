import numpy as np

h = np.arange(2,20,2).reshape(3,3)
h * 4
ident = np.eye(3,3)
print(h*ident)
print(np.matmul(ident,h))
