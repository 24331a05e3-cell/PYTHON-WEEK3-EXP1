#24331A05E3
#1D array
import numpy as np
array = input("Enter numerical values : ")
arr = np.array([int(x) for x in array.split()])
print("Given array:", arr)
n = int(input("Enter an index: "))
print("Element at index:", arr[n])
x = int(input("Enter start value to slice: "))
y = int(input("Enter end value to slice: "))
print("Sliced array:", arr[x:y])
