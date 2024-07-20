#Christina Pacheco
#July 7 2024
#p4HW1
#Assignment assess student ability to edit and enhance exiting programs

# Steps to follow:

# 1. Ask the user for the number of scores they want to enter
# 2. Create an empty list to store the scores
# 3. Start a loop to collect the scores from the user
# 4. Ask the user to inout a score
# 5. Check if the score is correct
# 6. If the score is wrong or a negative number, ask for a correct score until a right one is entered.
# 7. If the score is right (0 to 00), add it to the list.
# 8. After collecting all the scores, show the lowest score.
# 9. Remove the lowest score from the list and show the modified list.
# 10. Calculate the average of the remaining scores 
# 11. Determine the letter grade for the average 

import sys

def determine_letter_grade(average):
    if average >= 90:
        return 'A'
    elif average >= 80:
        return 'B'
    elif average >= 70:
        return 'C'
    elif average >= 60:
        return 'D'
    else:
        return 'F'

def main():
  
    try:
        num_scores = int(input("How many score do you want to enter?: "))
        if num_scores <= 0:
            print("Number of scores should be a positive integer.")
            return
    except ValueError:
        print("INVAILD Score entered!!! Score should be between 0 and 100.")
        return

    scores = []

    for i in range(num_scores):
        while True:
            try:
                score = float(input(f"Enter score #{i + 1}: "))
                if 0 <= score <= 100:
                    scores.append(score)
                    break
                else:
                    print("INVAILD Score entered!!! Score should be between 0 and 100.")
            except ValueError:
                print("Invalid input. Please enter a numerical value.")

    if not scores:
        print("No valid scores entered.")
        return

    print('-----------------------------Results-------------------------')


    lowest_score = min(scores)
    print(f"\nLowest score: {lowest_score}")

    
    scores.remove(lowest_score)
    print(f"Modified score list: {scores}")

   
    if scores:
        average_score = sum(scores) / len(scores)
        print(f"Average score: {average_score:.2f}")

      
        letter_grade = determine_letter_grade(average_score)
        print(f"Letter grade: {letter_grade}")
    else:
        print("No scores left to calculate the average.")

if __name__ == "__main__":
    main()
