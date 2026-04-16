# ASSIGNMENT A05 - SciPy Functions

import numpy as np
import matplotlib.pyplot as plt

print("----- BASIC NUMPY (USED IN SCIPY) -----")
print("Zeros:\n", np.zeros((2,3)))
print("Ones:\n", np.ones((2,3)))
print("Arange:", np.arange(7))
print("Linspace:", np.linspace(1, 4, 6))


print("\n----- MATRIX OPERATIONS -----")
mat = np.matrix('1 2; 3 4')
print("Matrix:\n", mat)
print("Transpose:\n", mat.T)
print("Conjugate Transpose:\n", mat.H)


print("\n----- SCIPY CONSTANTS -----")
from scipy.constants import pi
print("Value of PI:", pi)


print("\n----- FFT (FOURIER TRANSFORM) -----")
from scipy.fftpack import fft

x = np.array([1.0, 2.0, 1.0, -1.0, 1.5])
y = fft(x)
print("FFT:", y)


print("\n----- DCT (DISCRETE COSINE TRANSFORM) -----")
from scipy.fftpack import dct, idct

d = np.array([4., 3., 5., 10., 5., 3.])
print("DCT:", dct(d))
print("IDCT:", idct(d))


print("\n----- INTEGRATION -----")
from scipy.integrate import quad

result, _ = quad(lambda x: x**2, 0, 2)
print("Integration of x^2 from 0 to 2:", result)


print("\n----- INTERPOLATION -----")
from scipy.interpolate import interp1d

x = np.linspace(0, 4, 10)
y = np.cos(x)

f = interp1d(x, y, kind='linear')
xnew = np.linspace(0, 4, 20)

plt.figure()
plt.plot(x, y, 'o', xnew, f(xnew), '-')
plt.title("Interpolation")
plt.show()


print("\n----- LINEAR ALGEBRA -----")
from scipy import linalg

a = np.array([[3, 2, 0], [1, -1, 0], [0, 5, 1]])
b = np.array([2, 4, -1])

solution = linalg.solve(a, b)
print("Solution of linear equations:", solution)


print("\n----- IMAGE PROCESSING -----")
from scipy import ndimage

img = np.zeros((100, 100))
img[30:70, 30:70] = 1

blur = ndimage.gaussian_filter(img, sigma=2)

plt.figure()
plt.imshow(blur)
plt.title("Blur Image")
plt.show()


print("\n----- EDGE DETECTION -----")
sx = ndimage.sobel(img, axis=0)
sy = ndimage.sobel(img, axis=1)
sob = np.hypot(sx, sy)

plt.figure()
plt.imshow(sob)
plt.title("Edge Detection")
plt.show()


print("\n----- SPECIAL FUNCTIONS -----")
from scipy.special import cbrt, exp10, logsumexp

print("Cube root:", cbrt([10, 9, 0.1254]))
print("Exponential base 10:", exp10([2, 3]))
print("LogSumExp:", logsumexp(np.arange(10)))


print("\n----- PROGRAM COMPLETED -----")
