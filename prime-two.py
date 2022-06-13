num = 0

def is_prime(num):
    i = 5
    if(num <= 1):
        return False
    if(num <= 3):
        return True
    if((num % 2 == 0) or (num % 3 == 0)):
        return False
    while (i * i) <= num:
        if ((num % i == 0) or (num % (i + 2) == 0)):
            return False
        i = i + 6
    return True

take_input = input('Please enter any positive integer.')
converted_input = int(take_input)

if(is_prime(converted_input)):
    print(f'{converted_input} is Prime')
else:
    print(f'{converted_input} is not Prime')
    