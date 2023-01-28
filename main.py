from art import logo, vs
from game_data import data
import random

print(logo)
correct_answer = True
score = 0

dict_a = random.sample(data,1)
dict_b = random.sample(data,1)

while correct_answer:

    while dict_a == dict_b:
        dict_b = random.sample(data,1)

    print(f"Compare A: {dict_a[0]['name']}, a {dict_a[0]['description']}, from {dict_a[0]['country']}.")

    print(vs)

    print(f"Against B: {dict_b[0]['name']}, a {dict_b[0]['description']}, from {dict_b[0]['country']}.")

    user_input = input("Who has more followers. Type 'A' or 'B': ").upper()
    if user_input == 'A':
        if dict_a[0]['follower_count'] < dict_b[0]['follower_count']:
            correct_answer = False
        else:
            score += 1
            print(f"You are right. Current score: {score}")
    elif user_input == 'B':
        if dict_b[0]['follower_count'] < dict_a[0]['follower_count']:
            correct_answer = False
        else:
            score += 1
            print(f"You are right. Current score: {score}")
            
    dict_a = dict_b
    dict_b = random.sample(data,1)

print(logo)
print(f"Sorry, that's wrong. Final score {score}")
