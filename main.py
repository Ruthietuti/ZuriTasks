import random

while True:
    options = ["rock","paper","scissors"]
    R = "rock"

    CPU = random.choice(options)
    player = None

    while player not in options:
        player = input("Rock, Paper, or Scissors ?: ").lower()

    if player == CPU:
        print("CPU: ", CPU)
        print("player: ",player)
        print("Tie!")

    elif player == "rock":
        if CPU == "paper":
            print("CPU: ", CPU)
            print("player: ", player)
            print("You lose!")
        if CPU == "scissors":
            print("CPU: ", CPU)
            print("player: ", player)
            print("You win!")

    elif player == "scissors":
        if CPU == "rock":
            print("CPU: ", CPU)
            print("player: ", player)
            print("You lose!")
        if CPU == "paper":
            print("CPU: ", CPU)
            print("player: ", player)
            print("You win!")

    elif player == "paper":
        if CPU == "scissors":
            print("CPU: ", CPU)
            print("player: ", player)
            print("You lose!")
        if CPU == "rock":
            print("CPU: ", CPU)
            print("player: ", player)
            print("You win!")

    play_again = input("Play again? (yes/no): ").lower()

    if play_again != "yes":
        break

print("Winter is Coming!")