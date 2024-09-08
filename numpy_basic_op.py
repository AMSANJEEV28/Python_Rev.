import numpy as np

temperatures = np.array([[50, 51, 54, 59, 59, 53, 54, 51],
                         [45, 50, 38, 44, 40, 46, 43, 39]])

# Sum of each column
column_sums = np.sum(temperatures, axis=0)
print("Sum of each column:", column_sums)

# Sum of each row
row_sums = np.sum(temperatures, axis=1)
print("Sum of each row:", row_sums)
