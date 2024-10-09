import numpy as np

random_array = np.random.rand(1000)

filename = 'statistics_results.txt'
with open(filename, 'w+') as file:
    file.write(f'Average: {np.mean(random_array)}\n')
    file.write(f'Variance: {np.var(random_array)}\n')
    file.write(f'Standard Deviation: {np.std(random_array)}\n')

print(f'Results saved')
