import random

user_wins = 0
computer_wins = 0

options = ["rock", "paper", "scissors"] #List of answers

while True:
    user_input = input("Type Rock/Paper/Scissors, or Q to quit: ").lower()
    if user_input == "q":
        break

    if user_input not in options: 
        continue #If invalid answer is typed, go back to start of loop

    random_number = random.randint (0 , 2) 
    # 0 = rock, 1 = paper, 3 = scissors
    computer_pick = options[random_number]
    print("Computer choice", computer_pick + "." )

    #If statements to check for the win conditions
    if user_input == "rock" and computer_pick == "scissors":
        print("Nice!")
        user_wins += 1
        
    elif user_input == "paper" and computer_pick == "rock":
        print("Nice!")
        user_wins += 1
        
    elif user_input == "scissors" and computer_pick == "paper":
        print("Nice!")
        user_wins += 1

    elif user_input == computer_pick:
        print("Draw!")
        
    else:
        print("Take the L")
        computer_wins += 1

print("User wins" , user_wins, "times")
print("Computer wins" , computer_wins, "times")
print("Cyaaa")