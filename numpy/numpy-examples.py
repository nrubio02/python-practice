import numpy as np

nums_np = np.array(range(5))

print('===== Arrays =====')
# Numpy arrays are homogeneous. To print the datatype of the elements of the array:
print(nums_np.dtype)

# Numpy arrays allow array broadcasting, i.e you can apply an operation to all elements in the array by
# operating on the array variable. ** is power operator:
print(nums_np ** 2)

print('===== Indexing =====')
# Indexing in numpy arrays:
nums = [[1, 2, 3],
         [4, 5, 6]]
nums_np = np.array(nums)

print(nums_np[0, 1])

# Get the first column
print(nums_np[:, 0])

# Boolean indexing
nums = [-2, -1, 0, 1, 2]
nums_np = np.array(nums)
print(nums_np[nums_np > 0])
