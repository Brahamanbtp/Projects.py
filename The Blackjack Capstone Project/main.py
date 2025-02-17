import os
from art import logo 
import random

def clear():
    os.system("cls" if os.name == "nt" else "clear")  

def blackjack_game():
  
    def start_deal(cards):
        return random.choice(cards)

    def player_loss(player, cpu):
        return sum(player) != 21 and sum(cpu) == 21 or sum(player) == 21 and sum(cpu) == 21

    def done_playing():
        player_sum = sum(player_cards)
        cpu_sum = sum(cpu_cards)
        print(f"Your hand: {player_cards}, total: {player_sum}.")
        print(f"Computer's hand: {cpu_cards}, total: {cpu_sum}.")
        
        if cpu_sum > 21:
            print("The computer busted! You win!")
        elif player_loss(player_cards, cpu_cards):
            print("You lose.")
        elif player_sum == 21 and cpu_sum != 21:
            print("Blackjack! You win!")
        elif player_sum > 21:
            print("Bust! You lose.")
        elif player_sum == cpu_sum:
            print("It's a draw.")
        elif player_sum > cpu_sum:
            print("You win!")
        else:
            print("You lose.")

        play_again = input("Do you want to play again? (y/n): ").lower()
        if play_again == 'y':
            clear()
            blackjack_game()
        else:
            print("Goodbye!")

    def keep_playing():
        player_cards.append(start_deal(cards))
        cpu_cards.append(start_deal(cards))

        player_sum = sum(player_cards)
        cpu_sum = sum(cpu_cards)

        if 11 in player_cards and player_sum > 21:
            player_cards[player_cards.index(11)] = 1
            player_sum = sum(player_cards)

        print(f"Your hand: {player_cards}, total: {player_sum}.")
        print(f"Computer's hand: {cpu_cards}, total: {cpu_sum}.")

        if player_sum > 21:
            print("Bust! You lose.")
            done_playing()
        else:
            hit = input("Type 'y' to get another card, or 'n' to pass: ").lower()
            if hit == 'y':
                keep_playing()
            else:
                done_playing()


    print(logo)
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    player_cards = [start_deal(cards), start_deal(cards)]
    cpu_cards = [start_deal(cards)]

    print(f"Your cards: {player_cards}")
    print(f"Computer's first card: {cpu_cards}")

    hit = input("Type 'y' to get another card, or 'n' to pass: ").lower()
    if hit == 'y':
        keep_playing()
    else:
        done_playing()

blackjack_game()
