# Agueda Pacheco
# June 29th 2024
# P3LAB
# Assignment tests student's knowledge of how to write code that displays information to users




def calculate_change(amount):

    if amount == 0.00:
        return "No Change."
   
    amount_in_cents = int(amount * 100)

 
    dollars = amount_in_cents // 100
    amount_in_cents %= 100

    quarters = amount_in_cents // 25
    amount_in_cents %= 25

    dimes = amount_in_cents // 10
    amount_in_cents %= 10

    nickels = amount_in_cents // 5
    amount_in_cents %= 5

    pennies = amount_in_cents

   
    output = []

   
    if dollars > 0:
        if dollars == 1:
            output.append("1 dollar")
        else:
            output.append(f"{dollars} dollars")

    if quarters > 0:
        if quarters == 1:
            output.append("1 quarter")
        else:
            output.append(f"{quarters} quarters")

    if dimes > 0:
        if dimes == 1:
            output.append("1 dime")
        else:
            output.append(f"{dimes} dimes")

    if nickels > 0:
        if nickels == 1:
            output.append("1 nickel")
        else:
            output.append(f"{nickels} nickels")

    if pennies > 0:
        if pennies == 1:
            output.append("1 penny")
        else:
            output.append(f"{pennies} pennies")
            

    result = '\n'.join(output)
    return result

    

amount = float(input("Enter the amount of money as a float: $"))
print(calculate_change(amount))

