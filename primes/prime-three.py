import math as m
take_input = input('Please enter any positive integer.')
converted_input = int(take_input)

starting_point = 1
number_of_factors = 1

while starting_point <= m.sqrt(converted_input):
    if(converted_input % starting_point == 0):
        number_of_factors = number_of_factors + 1
    
    starting_point = starting_point + 1
    
print(f'Number of factors: {number_of_factors}')
    
    
if(number_of_factors == 2):
    print(f'{converted_input} is Prime')
else:
    print(f'{converted_input} is not Prime')
    
'''
Number of factors: 4
12 is not Prime

Number of factors: 9
568942365 is not Prime

Number of factors: 2
19991 is Prime

Number of factors: 2
4589756321 is Prime
'''
    
