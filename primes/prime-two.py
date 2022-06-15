import cProfile, pstats, io
from pstats import SortKey
pr = cProfile.Profile()
pr.enable()

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
    

pr.disable()
s = io.StringIO()
sortby = SortKey.CUMULATIVE
ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
ps.print_stats()
print(s.getvalue())


'''

Please enter any positive integer.987456321478963
987456321478963 is not Prime
         4 function calls in 3.305 seconds

   Ordered by: cumulative time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    3.305    3.305    3.305    3.305 {built-in method builtins.input}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
        1    0.000    0.000    0.000    0.000 /home/sanjib/Documents/development/discrete-python/primes/prime-two.py:8(is_prime)
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

'''