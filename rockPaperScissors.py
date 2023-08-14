import random

exit_game = False

user_score = 0
computer_score = 0

while not exit_game:
    options = ["rock", "paper", "scissors"]
    user_input = input("Choose rock, paper, scissors or exit: ").lower()

    if user_input == "exit":
        print("Game ended. Your Score:", user_score, "Computer Score:", computer_score)
        exit_game = True
    elif user_input in options:
        computer_input = random.choice(options)

        print(f"Your choice: {user_input}")
        print(f"Computer's choice: {computer_input}")

        if user_input == computer_input:
            print("It's a tie, no points awarded")
        elif (
            (user_input == "rock" and computer_input == "scissors") or
            (user_input == "paper" and computer_input == "rock") or
            (user_input == "scissors" and computer_input == "paper")
        ):
            user_score += 1
            print("You won!")
            print("Your Score:", user_score)
        else:
            computer_score += 1
            print("Computer won!")
            print("Computer Score:", computer_score)
    else:
        print("Invalid input. Please choose rock, paper, scissors, or exit.")
