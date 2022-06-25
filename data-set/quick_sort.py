import numpy as np

def arrange_in_ascending_order(generic_array, starting_number, ending_number):
        searching_index = generic_array[starting_number]
        low_index = starting_number + 1
        high_index = ending_number

        while True:            
            while low_index <= high_index and generic_array[high_index] >= searching_index:
                high_index = high_index - 1

            while low_index <= high_index and generic_array[low_index] <= searching_index:
                low_index = low_index + 1

            if low_index <= high_index:
                generic_array[low_index], generic_array[high_index] = generic_array[high_index], generic_array[low_index]
                
            else:                
                break

        generic_array[starting_number], generic_array[high_index] = generic_array[high_index], generic_array[starting_number]

        return high_index
def quickSort(generic_array_of_numbers, starting_number, ending_number):
        if starting_number >= ending_number:
            return

        partitioning_index = arrange_in_ascending_order(generic_array_of_numbers, starting_number, ending_number)
        quickSort(generic_array_of_numbers, starting_number, partitioning_index - 1)
        quickSort(generic_array_of_numbers, partitioning_index + 1, ending_number)

generic_array_of_numbers = [100, 45, 1, 8, 47895, 5, 56, 23, 0, 89]

quickSort(generic_array_of_numbers, 0, len(generic_array_of_numbers) - 1)
print("The above random generic_array of numbers in ascending order: " + str(generic_array_of_numbers))

np_array = np.array(generic_array_of_numbers)
sorting_np_array = np.sort(np_array, axis=None)

print(f'Sorting by NumPy sort method: {sorting_np_array}')

'''
The above random generic_array of numbers in ascending order: [0, 1, 5, 8, 23, 45, 56, 89, 100, 47895]
Sorting by NumPy sort method: [    0     1     5     8    23    45    56    89   100 47895]
'''