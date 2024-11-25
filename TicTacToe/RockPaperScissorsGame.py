import random

def get_choice():
    player_choice = input("Enter your choice(rock,paper,scissors): ")
    options=["rock","paper","scissors "]
    computer_choice = random.choice(options)
    choices={"player":player_choice,"computer":computer_choice}
    return choices

def check_win(player,computer):
    print(f"You chose {player}, computer chose {computer}")
    if player==computer:
        return "It's a tie!"
    elif player=="rock":
        if computer=="scissors":
            return "You win! Rock smashes scissors"
        else  :
           return "You lose. Paper covers rock"
    elif player=="scissors":
        if computer=="paper":
            return "You win! Scissors cut paper"
        else  :
           return "You lose. Rock smashes scissors"
    elif player=="paper":
        if computer=="scissors":
            return "You lose. Scissors cut paper"
        else  :
           return "You win! Paper covers rock"
       
choices = get_choice()
result = check_win(choices["player"],choices["computer"])
print(result)