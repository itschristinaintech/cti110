 # Agueda Pacheco
 # June 22, 2024
 # P2HW1
 # Assignment assess student ability to edit and enhance exiting programs

print('This program calculates and displays travel expenses.')
print()

print('Please enter your budget:', end=' ')
budget = float(input())
print()
print('Please enter your travel destination:', end=' ')
travel_location = input()
print()
print('How much will you spend on gas?', end=' ')
gas = float(input())
print()
print('How much will you spend on accommodation?', end=' ')
accommodation = float(input())
print()
print('How much will you spend on food?', end=' ')
food = float(input())
print()

result_expenses = gas + accommodation + food
result_remaining_balance = budget - result_expenses

print()
print('---------Travel Expenses--------')
print()

label_width = 20
value_width = 5

print(f"{'Travel location:':<{label_width}}{travel_location}")
print(f"{'Budget:':<{label_width}}${budget:>{value_width}.2f}")
print(f"{'Gas:':<{label_width}}${gas:>{value_width}.2f}")
print(f"{'Accommodation:':<{label_width}}${accommodation:>{value_width}.2f}")
print(f"{'Food:':<{label_width}}${food:>{value_width}.2f}")
print()
print('---------------------------------')
print(f"{'Remaining Balance:':<{label_width}}${result_remaining_balance:>{value_width}.2f}")

