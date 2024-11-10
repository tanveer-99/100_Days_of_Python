from art import logo
from art import vs
from game_data import data
import random


print(logo)
def comparefunc(compareA, compareB, point):

    winner = ''
    if compareA['follower_count'] > compareB['follower_count']:
        winner = 'a'
    else:
        winner = 'b'

    print(f"Compare A: {compareA['name']}, a {compareA['description']}, from {compareA['country']}")
    print(vs)
    print(f"Against B: {compareB['name']}, a {compareB['description']}, from {compareB['country']}")
    answer = input("Who has more followers? Type 'A' or 'B': ").lower()
    if answer == winner:
        point += 1
        comparefunc(compareB, data[random.randint(1,50)], point)
    else:
        print(f"Sorry, that's wrong. Final score: {point}")
        return



compareA = data[random.randint(1,50)]
compareB = data[random.randint(1,50)]
point = 0
comparefunc(compareA, compareB, point)