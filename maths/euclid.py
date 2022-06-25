def get_gcd(x, y):
    while x != y:
        if(x > y):
            x = x - y
        else:
            y = y - x
    return x
    
input_one = input('Please enter a number.')
input_two = input('Please enter another number')

x = int(input_one)
y = int(input_two)

print(f'Between {x} and {y} the GCD is {get_gcd(x, y)}')

