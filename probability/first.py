# we are to find the probability of finding an element in an array
    # it depends on two factors

    # Probability = number of favorable outcome / number of possible outcomes
    # number of possible outcomes is the length of the array
    # number of favourable outcome is the total number of the element in the list
    # Probability = total number of the element present / size or length of the array.

    # define the function to find the probability
def find_probability(the_array, the_length_of_array, the_element):
    count = the_array.count(the_element)
    # find probability up to 4 decimal places
    return round(count / the_length_of_array, 4)
    
the_array_variable = [22, 22, 22, 22, 22, 22, 22]
the_element_to_find = 22
the_length_of_array = len(the_array_variable)

print(f'The probability is: {find_probability(the_array_variable, the_length_of_array , the_element_to_find)}')