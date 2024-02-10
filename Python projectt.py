import random

userwins = 0
computerwins = 0
draws = 0
options = ["rock", "paper", "scissors"]

while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    
    if user_input == "q":
        break
    if user_input not in options:
        continue

    random_number = random.randint(0, 2)
    # rock: 0, paper: 1, scissors: 2
    computer_pick = options[random_number]
    print("Computer picked", computer_pick)

    if user_input == computer_pick:
        print("It's a draw!")
        draws += 1
    elif (user_input == "rock" and computer_pick == "scissors") or \
         (user_input == "paper" and computer_pick == "rock") or \
         (user_input == "scissors" and computer_pick == "paper"):
        print("You Won!")
        userwins += 1
    else:
        print("You Lost!")
        computerwins += 1

print("You Won", userwins, "times")
print("The computer won", computerwins, "times")
print("There were", draws, "draws.")
print("Goodbye")
