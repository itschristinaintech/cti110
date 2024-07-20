# Agueda Pacheco 
# June 22nd 2024
# p2LAB1
# Assignment tests student's knowledge of how to write code that performs mathematical calculations and displays information to users

import math

print('What is the radius of the cirle?', end=' ')
radius = float(input())

diameter = 2 * radius
print(f'The diameter of a circle is {diameter:.1f}')

circumference = 2 * math.pi * radius
print(f'The circumference of a circle is {circumference:.2f}')

area = math.pi * (radius * radius )
print(f'The area of a circle is {area:.3f}')

