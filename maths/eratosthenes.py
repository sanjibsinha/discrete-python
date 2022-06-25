def sieve_of_eratosthenes(range_of_numbers):    
    prime_array = [True for any_number in range(range_of_numbers + 1)]
    starting_number = 2
    while (starting_number * starting_number <= range_of_numbers):
        if (prime_array[starting_number] == True):
            for any_number in range(starting_number * 2, range_of_numbers + 1, starting_number):
                prime_array[any_number] = False
            starting_number += 1
            prime_array[0] = False
            prime_array[1] = False
        
        for starting_number in range(range_of_numbers + 1):
            if prime_array[starting_number]:
                print(starting_number)

sieve_of_eratosthenes(20)