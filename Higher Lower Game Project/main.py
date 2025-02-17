import os
from art import logo, vs  
from game_data import data 
import random


def clear():
    os.system("cls" if os.name == "nt" else "clear") 

def get_random_profile(exclude_name=None):
    while True:
        profile = random.choice(data)
        if profile['name'] != exclude_name: 
            return (
                f"{profile['name']}, a {profile['description']}, from {profile['country']}.",
                profile['follower_count']
            )

def higher_lower():
    score = 0
    profile_a, followers_a = get_random_profile()
    profile_b, followers_b = get_random_profile(exclude_name=profile_a.split(",")[0])

    while True:
        clear()
        print(logo)
        if score > 0:
            print(f"Correct! Your current score: {score}")

        print(f"\nCompare A: {profile_a}")
        print(vs)
        print(f"Compare B: {profile_b}")

        a_or_b = input("\nWho has more followers? Type 'a' or 'b': ").lower()

        if (a_or_b == 'a' and followers_a >= followers_b) or (a_or_b == 'b' and followers_b >= followers_a):
            score += 1
            if a_or_b == 'a':
                profile_b, followers_b = get_random_profile(exclude_name=profile_a.split(",")[0])
            else:
                profile_a, followers_a = profile_b, followers_b
                profile_b, followers_b = get_random_profile(exclude_name=profile_a.split(",")[0])
        else:
            print(f"\nIncorrect, your final score is {score}.")
            break

    play_again = input("\nDo you want to play again? Type 'y' or 'n': ").lower()
    if play_again == 'y':
        higher_lower()
    else:
        print("Thanks for playing!")

higher_lower()
