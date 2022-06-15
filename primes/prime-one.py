import math as m
import cProfile, pstats, io
from pstats import SortKey
pr = cProfile.Profile()
pr.enable()

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
    
print(f'Number of factors: {prime_check}')

if(prime_check == 2):
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
Number of factors: 8
987456321478963 is not Prime
         31423822 function calls in 8.130 seconds

   Ordered by: cumulative time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
 31423818    4.239    0.000    4.239    0.000 {built-in method math.sqrt}
        1    3.891    3.891    3.891    3.891 {built-in method builtins.input}
        2    0.000    0.000    0.000    0.000 {built-in method builtins.print}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


'''