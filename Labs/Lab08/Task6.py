import numpy as np

random_mat1 = np.random.choice([2,5,9,10],size=(5,3))
random_mat2 = np.random.choice([2,5,9,10],size=(3,2))
print(np.matmul(random_mat1,random_mat2))
print(np.multiply(random_mat1,random_mat2)) # does not work
