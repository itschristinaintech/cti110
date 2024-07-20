# Agueda Pacheco
# June 22nd 2024
# P2LAB2
# Assignment tests student's knowledge of how to write code that uses a dictionary to store user input and displays output to the user

cp_dict = {
    "keys": ["Camero", "Prius", "Model S", "Silverado"],
    "values": [18.21, 52.36, 110, 26]
}

keys = cp_dict["keys"]

print(keys)

print('Enter a vehicle to see its mpg:', end=' ')
car_input = input()

index = cp_dict["keys"].index(car_input)  
mpg = cp_dict["values"][index]    

print(f"The mpg for {car_input} is {mpg}.")

print(f"How many miles will you drive the {car_input}?", end=' ')
miles_input = int(input())

gallons_needed = miles_input / mpg

print(f"{gallons_needed:.2f} gallon(s) of gas are needed to drive the {car_input} {mpg}")




