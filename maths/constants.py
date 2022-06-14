import math as m

circumference_by_diameter = m.pi
#print(circumference_by_diameter)
# 3.141592653589793
# pi = c/d
diameter = 3
# if d = 3, c = pi * d
circumference = m.pi * diameter
# print(circumference)
# 9.42477796076938


circumference_by_radius = m.tau
print(circumference_by_radius)
# 6.283185307179586
# tau = c / r
# r = d / 2, c = tau * r
circumference = m.tau * (diameter / 2)
print(circumference)
# 9.42477796076938

eulers_number = m.e
print(eulers_number)
# 2.718281828459045

print(m.inf)
# inf

print(m.nan)
# nan

