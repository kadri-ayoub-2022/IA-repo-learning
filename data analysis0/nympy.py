import numpy as np

income = [-2, -1, 1, 2]
np.mean(income)  # calc the average
print("Absolute value: ", np.abs(income))  
print("Exponential: ", np.exp(income))
print("Logarithm: ", np.log(np.abs(income)))

income_array = np.array(income) # create numpy array

# np.zeros(n)  : creates an array of zeros consisting of n elements

# np.ones(n)  : similar to the above function, this one creates an array of ones

# np.arange(i, j, p)  : creates an array containing a linear sequence from i to j in steps of p

# np.linspace(i, j, n)  : creates an array of n evenly spaced values between i and j

# income_array.dtype  : access the element data type

# Elements starting from index no. 2
print(income_array[2:])

# array_name[condition]    income_array[(income_array > 2000) & (income_array < 3000)]

print(income_array.shape)
# (5,) we have an array containing 5 elements

# average
print(income_array.mean())

# return the index of min 
income_array.argmin()

# array  with 3 row and 5 column with value=1
np.ones((3, 5))

# a 6x3 table containing random values between 0 and 1
np.random.random((6, 3))

# a 3x3 table filled with random integers from 1 to 10
np.random.randint(1, 10, size=(3, 3))

np.full((2,2),4) # 2 x 2 with value of 4

# multiplication of matrix : AC = np.dot(A,C) == A@C
# np.matmul(a,b)  multiplication of matrix 

#condition in matrix:  mtrix[matrix[:,2] > 25]

#np.vstack((origin_array, new_info))([v1,v2])  add new rows

#np.identity(5)  identity matrix

#np.linalg.det(a) determinant of matrix

# a.reshape((2,1))