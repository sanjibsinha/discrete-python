def count_number_of_elements_in_array(the_array, match_element):
    count_numbers = 0
    for val in the_array:
        if val == match_element:
            count_numbers = count_numbers + 1
    return count_numbers

dice = [1, 2, 3, 4, 5, 6]
the_element = 2
length = len(dice)

total_number_of_elements = count_number_of_elements_in_array(dice, the_element)
the_probability = round(total_number_of_elements / length, 6)
print(f'The probability of getting 2 is: {the_probability}')

# The probability of getting 2 is: 0.166667
