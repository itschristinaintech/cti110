# Agueda Pacheco
# June 24th 2024
# P3HW2
# Assignment assess student understanding of decision structures

# Steps to follow:
# 1. Set your accumulator variables to zero
# 2. Start an indefinite loop to enter employee pay data
# 3. Ask the user to enter employee's name or 'Done' to terminate
# 4. If the user input is a name, calculate and show the pay statement for that employee
# 5. If the user input is 'done', accumulate totals for all entered employees and show the summaries
# 6. Calculate total pay variables for all entered employees when 'done' is entered.

total_overtime_pay = 0
total_reg_hour_pay = 0
total_gross_pay = 0
employee_count = 0


while True:
    employee_name = input("Enter employee's name or 'Done' to terminate: ")

    if employee_name.lower() == "done":
        break

    hours_worked = float(input("Enter number of hours worked: "))
    pay_rate = float(input("Enter employee's pay rate: "))
    
    if hours_worked > 40:
        overtime = hours_worked - 40
    else:
        overtime = 0

    overtime_pay_per_hour = pay_rate * 1.5
    overtime_pay = overtime * overtime_pay_per_hour
    reg_hour_pay = (hours_worked - overtime) * pay_rate
    gross_pay = reg_hour_pay + overtime_pay

    total_overtime_pay += overtime_pay
    total_reg_hour_pay += reg_hour_pay
    total_gross_pay += gross_pay
    employee_count += 1


    print()
    print(f'Employee Name: {employee_name}')
    print()
    print("Hours Worked      Pay Rate      OverTime       OverTime Pay    RegHour Pay   Gross Pay")
    print("--------------------------------------------------------------------------------" )
    print()
    print(f'{hours_worked:<18.2f}{pay_rate:<15.2f}{overtime:<15.2f}{overtime_pay:<15.2f}{reg_hour_pay:<13.2f}{gross_pay:<13.2f}')

print()

print(f'Total number of employees entered: {employee_count}')
print(f'Total overtime pay: {total_overtime_pay:.2f}')
print(f'Total regular pay: {total_reg_hour_pay:.2f}')
print(f'Total gross pay: {total_gross_pay:.2f}')
