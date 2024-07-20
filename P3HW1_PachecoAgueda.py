# Agueda Pacheco 
# June 29th 2024
# P3HW1
# This program takes a number grade , determines average and displays letter grade for average.

# Enter grades for six modules

mod_1 = float(input('Enter grade for Module 1: '))
mod_2 = float(input('Enter grade for Module 2: '))
mod_3 = float(input('Enter grade for Module 3: '))
mod_4 = float(input('Enter grade for Module 4: '))
mod_5 = float(input('Enter grade for Module 5: '))
mod_6 = float(input('Enter grade for Module 6: '))

# Add grades entered to a list

grades = [mod_1, mod_2, mod_3, mod_4, mod_5]

# Define list width

label_width = 20

print()

print('-----------Results--------------')
# Determine lowest, highest , sum and average for grades

min_grade = min(grades)
print(f"{'Lowest Grade:':<{label_width}}{min_grade}")

max_grade = max(grades)
print(f"{'Highest Grade:':<{label_width}}{max_grade}")

sum_of_grades = sum(grades)
print(f"{'Sum of Grades:':<{label_width}}{sum_of_grades}")

avg_of_grades = sum_of_grades / len(grades)
print(f"{'Average:':<{label_width}}{avg_of_grades}")

# Determine letter grade for average

print()

print('-------------------------')

if avg_of_grades >= 90:
    print('Your grade is: A')
    
elif avg_of_grades >= 80:
    print('Your grade is: B')
    
elif avg_of_grades >= 70:
    print('Your grade is: C')
    
elif avg_of_grades >= 60:
    print('Your grade is: D')
    
else:
    print('Your grade is: F')
  
    






