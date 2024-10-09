import numpy as np

odd_mat = np.array(np.arange(1,33,2)).reshape(4,4)
random_mat = np.random.choice([2,5,9,10],size=(4,4))
print(np.matmul(odd_mat,np.matmul(random_mat,np.eye(4,4))))
