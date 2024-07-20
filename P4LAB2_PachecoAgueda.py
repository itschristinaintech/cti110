#Agueda Pacheco
#July 7 2024
#p4LAB2
#Assignment tests student's knowledge of how to write code that displays information to users using loops.



def multiplication_table(n):
    for i in range(1, 13):
        print(f"{n} x {i} = {n * i}")

def main():
    while True:
        user_input = int(input("Enter an integer: "))
        
        if user_input >= 0:
            multiplication_table(user_input)
        else:
            print("This program cannot accept negative values.")
        
        run_again = input("Do you want to run the program again? (yes/no): ")
        if run_again != "yes":
            break

if __name__ == "__main__":
    main()

