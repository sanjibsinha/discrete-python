import numpy as np

mean = 0.0
median = 0.0

def find_mean(the_array, num):
  sum = 0.0
  i = 0
  while(i < num):
    sum = sum + the_array[i]
    i = i + 1
  mean = sum / num
  return mean
the_array = np.array([1, 2, 3, 4, 5, 3, 2, 568, 1200])
length_of_array = len(the_array)
print(f'Mean from original program: {find_mean(the_array, length_of_array)}')
numpy_mean = np.mean([1, 2, 3, 4, 5, 3, 2, 568, 1200])
print(f'Mean from NumPy Mean: {numpy_mean}')

'''
Mean from original program: 198.66666666666666
Mean from NumPy Mean: 198.66666666666666
'''