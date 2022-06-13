import math as m
take_input = input('Please enter any positive integer.')
converted_input = int(take_input)

prime_check = 0
starting_point = 1

while starting_point <= m.sqrt(converted_input):
    # 
    if(converted_input % starting_point == 0):
        if(converted_input / starting_point == 2):
            prime_check = prime_check + 1
        else:
            prime_check = prime_check + 2
    starting_point = starting_point + 1


if(prime_check == 2):
    print(f'{converted_input} is Prime')
else:
    print(f'{converted_input} is not Prime')