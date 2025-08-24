import random

def rps_game():
    # Plays Rock-Paper-Scissors using a lookup table approach.

    choices = ["rock", "paper", "scissors"]
    results = {
        ("rock", "rock"): "tie",
        ("rock", "paper"): "computer",
        ("rock", "scissors"): "user",
        ("paper", "rock"): "user",
        ("paper", "paper"): "tie",
        ("paper", "scissors"): "computer",
        ("scissors", "rock"): "computer",
        ("scissors", "paper"): "user",
        ("scissors", "scissors"): "tie",
    }
    scores = {"user": 0, "computer": 0}

    while True:
        print("\nRock-Paper-Scissors")
        user_input = input("Enter rock, paper, scissors, or quit: ").lower()

        if user_input == "quit":
            print(f"\nFinal Score: User: {scores['user']}, Computer: {scores['computer']}")
            print("Thanks for playing!")
            break

        if user_input not in choices:
            print("Invalid input. Please choose rock, paper, or scissors.")
            continue

        computer_input = random.choice(choices)
        print(f"Computer chose: {computer_input}")

        outcome = results[(user_input, computer_input)]

        if outcome == "tie":
            print("It's a tie!")
        elif outcome == "user":
            print("You win!")
            scores["user"] += 1
        else:
            print("Computer wins!")
            scores["computer"] += 1

        print(f"Score: User: {scores['user']}, Computer: {scores['computer']}")

rps_game()
