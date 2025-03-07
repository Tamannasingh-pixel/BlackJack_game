# ---------------------------- CAPSTONE PROJECT - 1 ----------------------------
# ------------------------------- BLACKJACK GAME -------------------------------

import random
import os
from blackjack_ascii_art import cards
from blackjack_ascii_art import logo
from blackjack_ascii_art import thank_you
from blackjack_ascii_art import win
from blackjack_ascii_art import lose
from blackjack_ascii_art import draw

def clear_screen():
                if os.name == 'nt':
                    os.system('cls')

def play_blackjack(start):
    keys = list(cards.keys())

    # computer card 1 choice and its value
    computer_random_card_1 = random.choice(keys)
    computer_card_1_value = cards[computer_random_card_1]

    # computer card 2 choice and its value (hidden for the player)
    computer_random_card_2 = random.choice(keys)
    computer_card_2_value = cards[computer_random_card_2]

    # your card 1 choice and its value 
    your_random_card_1 = random.choice(keys)
    your_card_1_value = cards[your_random_card_1]

    # your card 2 coice and its value
    your_random_card_2 = random.choice(keys)
    your_card_2_value = cards[your_random_card_2]

    # your card 3 coice and its value
    your_random_card_3 = random.choice(keys)
    your_card_3_value = cards[your_random_card_3]

    if start == "y":
        print(logo)
        print(f"computer cards: {computer_random_card_1} \n") # computer_card_2 is secret
        print(f"computer total = {computer_card_1_value} + ? \n")

        print(f"your cards: {your_random_card_1} \n{your_random_card_2} \n")
        print(f"your total = {your_card_1_value + your_card_2_value}\n")

        # another_card = input("do you want to draw another card, type 'y' for yes or 'n' for no : ").lower()
        def another_deal(another_card):

            if another_card == "y":

                print(f"your next card is: {your_random_card_3}\n")

                your_total = your_card_1_value + your_card_2_value + your_card_3_value
                print(f"your total: {your_total}\n")

                computer_total = computer_card_1_value + computer_card_2_value
                print(f"computer total is {computer_total}\n")

                if your_total <= 21 and computer_total <= 21:

                    if (21 - your_total) == (21 - computer_total):
                        print(draw)    
                    elif (21 - your_total) >= (21 - computer_total):
                        print(lose)
                    elif (21 - your_total)<= (21 - computer_total):
                        print(win)
                        
                elif your_total > 21 and computer_total <= 21:
                    print(lose)
                elif computer_total > 21 and your_total <= 21:
                    print(win)
                

            if another_card == "n":
                your_total = your_card_1_value + your_card_2_value
                print(f"your total is: {your_total}\n")

                computer_total = computer_card_1_value + computer_card_2_value
                print(f"computer total is {computer_total}\n")

                if your_total <= 21 and computer_total <= 21:

                    if (21 - your_total) == (21 - computer_total):
                        print(draw)
                    elif (21 - your_total) >= (21 - computer_total):
                        print(lose)
                    elif (21 - your_total)<= (21 - computer_total):
                        print(win)
                        
                elif your_total > 21 and computer_total <= 21:
                    print(lose)
                elif computer_total > 21 and your_total <= 21:
                    print(win)
        
        another_deal(input("do you want to draw another card, type 'y' for yes or 'n' for no : ").lower())
            

    elif start == "n":
        print(thank_you)
    # play_again = input("do you want to play another game of blackjack 'y' for yes and 'n' for no :  ")

while True:
    play_blackjack(input("do you want to play blackjack, type 'y' for yes or 'n' for no:  ").lower())
    def play_again(play_it_again): 
        if play_it_again == "y":
            clear_screen()
            play_blackjack(input("do you want to play blackjack, type 'y' for yes or 'n' for no:  ").lower())
                # play_again
        elif play_it_again == "n":
            clear_screen()
            print(thank_you)
        # break #exit the main while loop, ending the program
        else:
            print("Invalid input. Please enter 'y' or 'n'")
    
    play_again(input("Do you want to play another game of Blackjack? Type 'y' or 'n': "))

