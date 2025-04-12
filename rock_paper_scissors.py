import random


def get_choices() -> dict:
    options = ["rock", "paper", "scissors"]
    player_choice = input("Enter a choice (rock, paper or scissors): ")

    while player_choice.lower() not in options:
        print(f"{player_choice} is not in the options.")
        player_choice = input("Enter a choice (rock, paper or scissors): ")

    computer_choice = random.choice(options)

    choices = {"player": player_choice, "computer": computer_choice}

    return choices

def check_win(player, computer):
    print(f"You chose {player.upper()}\nComputer chose {computer.upper()}")

    if player == computer:
        return f"It's tie! You both chose {player.upper()}"
    elif player == "rock":
        if computer == "scissors":
            return f"ROCK smashes SCISSORS! You WIN!"
        else:
            return f"PAPER covers ROCK! You LOSE!"
    elif player == "paper":
        if computer == "scissors":
            return f"SCISSORS cuts PAPER! You LOSE!"
        else:
            return f"PAPER covers ROCK! You WIN!"
    elif player == "scissors":
        if computer == "paper":
            return f"SCISSORS cuts PAPER! You WIN!"
        else:
            return f"ROCK smashes SCISSORS! You LOSE!"


choices = get_choices()
print(check_win(choices['player'], choices['computer']))
