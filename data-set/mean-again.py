import numpy as np

print('hello')

def get_median(the_array, num):
  # we know that median varies due to the odd and even numbers
  # let us sort the array first
  the_array.sort()
  # next check for the even case
  if (num % 2 != 0):
    even = num // 2
    median = the_array[(even)]
    return median
  else:
    # check for the odd case
    median = (the_array[(num - 1) / 2] + the_array[num / 2]) / 2.0
    return median

the_array = np.array([1, 2, 3, 4, 5, 3, 2, 568, 1200])
print(the_array) 
length = np.count_nonzero(the_array)


print(f'Median: {get_median(the_array, length)}')
print(f'Median from NumPy: {np.median(the_array)}')
  
  
'''
hello
[   1    2    3    4    5    3    2  568 1200]
Median: 3
Median from NumPy: 3.0
'''