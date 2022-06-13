import math as m
take_input = input('Please enter any positive integer.')
converted_input = int(take_input)

starting_point = 1
number_of_factors = 1

while starting_point <= m.sqrt(converted_input):
    if(converted_input % starting_point == 0):
        number_of_factors = number_of_factors + 1
    
    starting_point = starting_point + 1
    
    
if(number_of_factors == 2):
    print(f'{converted_input} is Prime')
else:
    print(f'{converted_input} is not Prime')
    

    
