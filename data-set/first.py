import numpy as np
import matplotlib.pyplot as plt

a = np.array([
    [1, 2], 
    [0, 1]
])

b = np.array([
    [2, 0], 
    [3, 4]
])

# matrix_product = np.dot(a, b)
matrix_product = a @ b
print(a @ b)
'''
[[8 8]
 [3 4]]
'''

# plt.imshow(a, interpolation='nearest')
#plt.imshow(b, interpolation='nearest')
plt.imshow(matrix_product, interpolation='nearest')
plt.show()