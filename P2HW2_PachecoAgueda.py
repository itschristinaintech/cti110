#Agueda Pacheco

#June 22 2024

#P2HW2

#Assignment assess student understanding of Lists

#Create an empty list module_grades

module_grades = []

# 1. Prompt user to enter grade for Module 1
# 2. Read the integer input as module1_test
# 3. Append `module1_test` to module_grades
# 3. Repeat stpes 1 - 4 for each module
# Reminder: Be sure to change the module # for each string value

print('Enter grade for Module 1:', end=' ')
module1_test = int(input())
module_grades.append(module1_test)
print('Enter grade for Module 2:', end=' ')
module2_test = int(input())
module_grades.append(module2_test)
print('Enter grade for Module 3:', end=' ')
module3_test = int(input())
module_grades.append(module3_test)
print('Enter grade for Module 4:', end=' ')
module4_test = int(input())
module_grades.append(module4_test)
print('Enter grade for Module 5:', end=' ')
module5_test = int(input())
module_grades.append(module5_test)
print('Enter grade for Module 6:', end=' ')
module6_test = int(input())
module_grades.append(module6_test)
print()
print('-----------Results----------')
print()

# Define the length and width for formatting

label_width = 20
value_width = 5

# Find and print the lowest grade in the list
lowest_grade = min(module_grades)
print(f"{'Lowest grade:':<{label_width}} {lowest_grade:>{value_width}}")

# Find and print the highest grade in the list
highest_grade = max(module_grades)
print(f"{'Highest grade:':<{label_width}} {highest_grade:>{value_width}}")

# Calculate and print the sum of the grades
sum_grade = sum(module_grades)
print(f"{'Sum of grades:':<{label_width}} {sum_grade:>{value_width}}")

# Calculate and print the average of the grades
average_grade = sum_grade / len(module_grades)
print(f"{'Average grade:':<{label_width}} {average_grade:.2f}")

