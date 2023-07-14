import random
from art import logo
import os 
clear=lambda:os.system('cls')

is_game_over=False


def choseCard():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    chosen_card=random.sample(cards,2)
    return chosen_card

def choseSingleCard():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def calculateSum(cards):
    if sum(cards)==21:
        return 0
    if 11 in cards and sum(cards)>21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(computer_score,user_score):
    if computer_score==0:
        print("Lose, Opponent has BlackJack!")
    elif user_score==0:
        print("Win with a BlackJack!")
    elif user_score>21:
        print("Bust! you Lose!")
    elif user_score==computer_score:
        print("Draw!")
    elif computer_score>21:
        print("You Win!")
    elif user_score>computer_score:
        print("You Win!")
    else:
        print("You Lose!")


def playGame():
    is_game_over=False
    print(logo)
    computer_cards=[]
    user_cards=[]
    computer_cards=choseCard()
    user_cards=choseCard()



    while not is_game_over:
        user_score=calculateSum(user_cards)
        computer_score=calculateSum(computer_cards)
        print(f"Your cards: {user_cards} current score {sum(user_cards)}")

        if user_score==0 or computer_score==0 or user_score >21:
            is_game_over=True  
        else:
            user_deal=input("Type 'y' to get another card, type 'n' to pass: ")
            if user_deal=='y':
                user_cards.append(choseSingleCard())
            else:
                is_game_over="True"

    while computer_score!=0 and computer_score < 17 :
        computer_cards.append(choseSingleCard())
        computer_score=calculateSum(computer_cards)

    print(f"Your final hand: {user_cards}, final score: {sum(user_cards)}")
    print(f"Computer's final hand: {computer_cards}, final score: {sum(computer_cards)}")
    compare(computer_score,user_score)

while input("Do you want to play a game of BlackJack? Type 'y' or 'n' : ")=='y':
    clear()
    playGame()
    

