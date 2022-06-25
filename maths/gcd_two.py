def get_gcd_first_method(number_one, number_two):
    if(number_two == 0):
        return number_one
    else:
        temporary_storage = number_one % number_two
        return get_gcd_first_method(number_two, temporary_storage)


def get_gcd_second_method(number_one, number_two):
    if(number_two == 0):
        return number_one
    elif(number_one > number_two):
        return get_gcd_second_method((number_one - number_two), number_two)
    else:
        return get_gcd_second_method((number_two - number_one), number_one)


print(get_gcd_first_method(1071, 462))
print(get_gcd_second_method(1071, 462))