#Juego de Piedra papel o tijera
import random

def get_choices():
    player_choice = input("Enter a choice (rock, paper, scissors): ")
    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)
    choices = {"player":player_choice,"computer":computer_choice}
    return choices

def check_win(player, computer):
    '''print("You chose " + player + ", computer chose " + computer)''' #Concatenation
    print(f"You chose {player}, computer chose {computer}")
    if player == computer:
        return "It's a tie"
    elif player == "rock":
        if computer == "scissors":
            return "Rock smashes scissors! you win!!!"
        else:
            return "Paper covers rock, you lose (pediste :D)."
    elif player == "paper":
        if computer == "scissors":
            return "Scissors cuts paper, you lose (pediste :D)."
        else:
            return "Paper covers rock! you win!!!"
    elif player == "scissors":
        if computer == "paper":
            return "Scissors cuts paper! you win!!!"
        else:
            return "Rock smashes scissors, you lose (pediste :D)."

choices = get_choices()
result = check_win(choices["player"], choices["computer"])

print(result)
