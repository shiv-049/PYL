# ASSIGNMENT A01 - NumPy Functions

import numpy as np

print("----- NUMPY ARRAY CREATION -----")
# 1. Creating arrays
a = np.array([1, 2, 3])
print("1D Array:", a)

b = np.array([[1, 2], [3, 4]])
print("2D Array:\n", b)

# Minimum dimension
c = np.array([1, 2, 3, 4, 5], ndmin=2)
print("Array with minimum 2 dimensions:\n", c)


print("\n----- DATA TYPES -----")
# 2. Data type
dt = np.dtype(np.int32)
print("Data type:", dt)

x = np.array([1, 2, 3, 4, 5], dtype=np.int8)
print("Array with int8:", x)
print("Item size (bytes):", x.itemsize)


print("\n----- ARRAY ATTRIBUTES -----")
# 3. Array attributes
arr = np.array([[1, 2, 3], [4, 5, 6]])
print("Shape:", arr.shape)
print("Dimensions:", arr.ndim)


print("\n----- SPECIAL ARRAYS -----")
# 4. zeros and ones
z = np.zeros(5)
print("Zeros array:", z)

o = np.ones((2, 2), dtype=int)
print("Ones array:\n", o)

# empty array
e = np.empty((2, 2))
print("Empty array:\n", e)


print("\n----- ARRAY FROM EXISTING DATA -----")
# 5. asarray
lst = [1, 2, 3]
arr1 = np.asarray(lst)
print("Array from list:", arr1)

# frombuffer
s = b'Hello World'
arr2 = np.frombuffer(s, dtype='S1')
print("Array from buffer:", arr2)

# fromiter
it = iter([0, 1, 2, 3, 4])
arr3 = np.fromiter(it, dtype=float)
print("Array from iterator:", arr3)


print("\n----- ARRAY FROM NUMERICAL RANGE -----")
# 6. arange
ar = np.arange(5)
print("Arange:", ar)

ar_float = np.arange(5, dtype=float)
print("Arange with float:", ar_float)

# linspace
ls = np.linspace(0, 10, 5)
print("Linspace:", ls)


print("\n----- PROGRAM COMPLETED -----")
