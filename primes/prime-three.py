import math as m
import cProfile, pstats, io
from pstats import SortKey
pr = cProfile.Profile()
pr.enable()



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
    
    
pr.disable()
s = io.StringIO()
sortby = SortKey.CUMULATIVE
ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
ps.print_stats()
print(s.getvalue())
    
'''

Please enter any positive integer.987456321478963
Number of factors: 5
987456321478963 is not Prime
         31423822 function calls in 8.300 seconds

   Ordered by: cumulative time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
 31423818    4.265    0.000    4.265    0.000 {built-in method math.sqrt}
        1    4.035    4.035    4.035    4.035 {built-in method builtins.input}
        2    0.000    0.000    0.000    0.000 {built-in method builtins.print}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

'''
    
