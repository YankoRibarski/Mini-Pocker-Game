import random
print("Welcome to our Casino.\nWe are going to play a game,named mini pocker")
print("********************************************************")
first_player_name = input("Please enter your name:")
print(f"OK {first_player_name},you are going to play against the computer\n********************************************************")

playing_cards = ["9","10","Jack","Queen","King"]
counter = 0
player_points = 0
computer_points = 0
for i in range(4):
    current_card = random.choice(playing_cards)
    counter += 1


    if counter % 2 != 0:
        print(f"your  card is:{current_card}")
        player_cards = current_card
        if player_cards == "9":
            player_points += 9
        elif player_cards == "10":
            player_points += 10
        elif player_cards == "Jack":
            player_points += 11
        elif player_cards == "Queen":
            player_points += 12
        elif player_cards == "King":
            player_points += 13


    else:
        print(f"computer  card is:{current_card}")
        computer_cards = current_card
        if computer_cards == "9":
            computer_points += 9
        elif computer_cards == "10":
            computer_points += 10
        elif computer_cards == "Jack":
            computer_points += 11
        elif computer_cards == "Queen":
            computer_points += 12
        elif computer_cards == "King":
            computer_points += 13

print(f"your result is:{player_points}\ncomputer result is:{computer_points}")
if player_points > computer_points:
    print("YOU WIN!!!")
elif player_points == computer_points:
    print("IT'S DEUCE,YOU NEED TO PLAY AGAIN!!!")
else:
    print("YOU LOSS")
