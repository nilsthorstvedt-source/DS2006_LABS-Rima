
import copy
import random
import dice_collection

print("🎲 Welcome to Battle of Dices! 🎲")


# variables to keep track of the score:
rounds = 0
gameover = False
# number of wins needed to win the game:
winning_score = 3

# dictionary template for storing player information:
player_info = {
    "name": "",
    "email": "",
    "country": "",
    "wins": 0,
    "rolls": []
}

# list to store the dicts for each player:
players = []

# obtain the number of players:
number_of_players = int(input("how many players?"))

# for loops to obtain the player names:
for i in range(number_of_players):

    # make a deep copy of the template for this player:
    player = player_info.copy()

    player["name"] = input(f"what is the name of player {i + 1}?")
    player["email"] = input(f"what is the email of player {i + 1}?")
    player["country"] = input(f"what is the country of player {i + 1}?")

    players.append(player)


# repeat until the game is over, as many rounds as necessary:
while gameover is False:

    print(f"round {rounds + 1}:")

    # dice roll for each player in the current round:
    current_rolls = []

    # we need to roll the dice for each player:
    for each_player in players:
        roll = dice_collection.D6()

        # player roll history
        each_player["rolls"].append(roll)

        current_rolls.append(roll)

        print(f"player {each_player['name']} rolled: {roll}")

    # obtain the highest roll this round:
    max_roll = max(current_rolls)

    # find winners of the round:
    winners = []

    # search for all players who got the highest roll:
    for each_player in players:
        if (each_player["rolls"][-1] == max_roll):
            each_player["wins"] += 1
            print(f"player {each_player['name']} won in round {rounds + 1}")

            winners.append(each_player['name'])

    print(f"winners of this round: {winners}")

    for each_player in players:
        if (each_player["wins"] >= winning_score):
            print(
                f"\n {each_player['name']} is the newest battle of dices champion!")
            gameover = True

    if gameover is False:
        print("this heated battle of dices is still going on, who will win at the end?")
    rounds += 1

# save results to file
filename = input("enter the filename to save the results: ")
with open(filename, "w") as file:  # "w" = write mode
    # player information:
    file.write("player information:\n")

    # saves each player information
    for each_player in players:
        file.write(
            f"name: {each_player['name']}\n"
            f"email: {each_player['email']}\n"
            f"country: {each_player['country']}\n"
            f"wins: {each_player['wins']}\n\n"
        )
    file.write("\n game rounds: \n")

    # round history
    for r in range(rounds):
        # start with empty text for this round
        rolls_str = ""

        # go through each player and build the string step by step
        for i, each_player in enumerate(players):
            rolls_str += f"{each_player['name']} rolled {each_player['rolls'][r]}"

            # add a comma and space until last player
            if i < len(players) - 1:
                rolls_str += ","
            # now write the full round info to the file
        file.write(f"round {r+1}:\n {rolls_str}\n")
        print("\n game over! results saved successfully")
