#Sample Numpy Code
import numpy as np

#Build an array, outputs 0,1,2,3
a = np.arange(4)
print('here is the array: ', a)

#Build a multi-dimensional array
b = np.arange(15).reshape(3,5)
print('here is the multi dimensional array: ', b)

#build an array that steps by two, starts at 30 and ends at 60
c = np.arange(30,60,2)
c

#build an array and double the values in the array
d = np.arange(15)
e = d*2
print('here is the doubled array: ',e)

#build an array with equally spaced values
f = np.linspace(3,9,5)
print('here are five values between 3 and 9: ',f)

#indexing
g = f[2]
print('here is the third value from the previous array: ',g)

#slicing
x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
h = c[0:5]
print('here are all items in the array with an index lower than five: ',h)