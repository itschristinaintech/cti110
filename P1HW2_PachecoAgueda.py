 # Agueda Pacheco
 # June 15, 2024
 # P1HW2
 # For this assignment you will create a program that does some basic math on numbers that are entered. 

print('This program calculates and displays travel expenses.')


print('Please enter your budget:', end=' ')
budget = float(input())
print('Please enter your travel destination:', end=' ')
travel_location = input()
print('How much will you spend on gas?', end=' ')
gas = float(input())
print('How much will you spend on accommodation?', end=' ')
accommodation = float(input())
print('How much will you spend on food?', end=' ')
food = float(input())

result_expenses = gas + accommodation + food
result_remaining_balance = budget - result_expenses

print('---------Travel Expenses--------')

print(f"Travel location:{travel_location}")
print(f"Budget:{budget}") 


print(f"Gas:{gas}")
print(f"Accommodation:{accommodation}")
print(f"Food:{food}") 


print(f"Remaining Balance:{result_remaining_balance}")

