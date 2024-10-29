import numpy as np
import abc as ab
import seaborn as sb
import pandas as pd
import matplotlib.pyplot as plt

# Separate dataset and age groups used to accomodate that dataset as the specified dataset was not provided

arr0 = np.array(np.arange(1,10))
print(f"Original Array: {arr0}\nArray Sum: {arr0.sum()}\nArray Mean: {arr0.mean()}\nArray Product: {arr0.prod()}")

mat0 = np.array(np.random.randint(100,size=(3,3)))
print(f"Original Matrix: \n{mat0}\nMatrix Transpose: \n{mat0.transpose()}")

reshapable_array = np.array(np.arange(1,21))
print(f"Original Array: {reshapable_array}\nReshaped Array: \n{reshapable_array.reshape((4,5))}")

arr1 = np.array(np.arange(1,10))
arr2 = np.array(np.arange(11,20))
print(f"Array 1: {arr1}\nArray 2: {arr2}\nSum of Arrays: {arr1+arr2}\nDifference of Arrays: {arr1-arr2}\nProduct of Arrays: {arr1*arr2}\nQuotient of Arrays: \n{arr1/arr2}")

arr3 = np.array(np.arange(1,11))
print(f"Original Array: {arr3}\nAfter Square Root: \n{np.sqrt(arr3)}")

mat1 = np.array(np.random.randint(100,size=(2,2)))
print(f"Original Matrix:  \n{mat1}\nMatrix Determinant: {np.linalg.det(mat1)}\nMatrix Inverse: \n{np.linalg.inv(mat1)}")

arr4 = np.array(np.random.randint(100,size=50))
print(f"Original Array: \n{arr4}\nMaximum Element: {arr4.max()}\nMinimum Element: {arr4.min()}")

mat2 = np.array(np.random.randint(10,size=(3,3)))
RHS_Vector = np.array(np.random.randint(10,size=(3,1)))
print(f"Co-efficient Matrix: \n{mat2}\nRight Hand Side Vector: \n{RHS_Vector}\nSolution Vector: \n{np.linalg.solve(mat2,RHS_Vector)}")

arr5 = np.array(np.random.randint(100,size=25))
print(f"Original Array: \n{arr5}\n75th Percentile: {np.percentile(arr5,75)}")

def Normalize(x) :
    return (x - np.mean(x)) / np.std(x)
arr6 = np.array(np.random.randint(100,size=50))
print(f"Original Array: \n{arr6}\nNormalized Array: \n{Normalize(arr6)}")
