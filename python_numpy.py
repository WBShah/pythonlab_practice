import numpy as np

# creating a numpy array
arr = np.array([1,2,3,4,5])
print(arr)
# output: [1 2 3 4 5]

# Performing mathematical operations on the array - adds +2 for each value
arr += 2 
print(arr)
# output: [3 4 5 6 7]

# array squared
arr_squared = arr ** 2
print (arr_squared)
# output [ 9 16 25 36 49 ]


# Accessing elements in the array
print(arr[2])
# output 5

# slicing the array
print(arr[1:4])
#output: [4 5 6]

# performing aggregate operations on the array
arr_sum = np.sum(arr)
print(arr_sum)
# output: 25

# Calculate the mean of all elements 
arr_mean = np.mean(arr)
print(arr_mean)
# Output: 5.0

# append array to make it long enough to create a 2x3 matrix 
value = 8
arr_append = np.append(arr,value)
print(arr_append)


# reshaing the array
arr_2d = arr_append.reshape([2,3])
print(arr_2d)

# creating special type of arrays
zeros_arr = np.zeros((3,2))
print(zeros_arr)

ones_arr = np.ones((2,4))
print(ones_arr)

random_arr = np.random.rand(3,3)
print(random_arr)
