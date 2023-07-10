from ai import *
from helper import *

def get_input():
    """
    Gets an input from the user.
    """
    while True:
        choice = input("Enter your choice: [Rock (R), Paper (P), Scissor (S)]\n> ")
        choice = choice.strip().lower()

        if choice not in ["rock", "paper", "scissor", "r", "p", "s"]:
            print("Wrong input. Please enter from the options only.")
        else:
            break

    if choice in ["rock", "r"]:
        return "r"
    elif choice in ["paper", "p"]:
        return "p"
    else:
        return "s"

def current_round():
    """
    Provides the data for the current round.
    """
    ai_choice = choose_model()
    choice = get_input()

    print(f"User - {return_choice(choice)} : {return_choice(ai_choice)} - Computer")

    current = declare_winner(choice, ai_choice)
    rate_all_models(choice)

    if current != "Draw":
        print(f"This round has been won by {current}.")
    else:
        print(f"This round is a draw.")

    tally_scores(current)

#__main__
print("Rock, Paper, Scissor game")
clean_logs()
for i in range(10):
    current_round()
find_ai_accuracy()