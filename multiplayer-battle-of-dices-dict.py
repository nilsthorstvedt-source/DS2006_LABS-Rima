# 🎲 Battle of Dices (Dictionary-Based, Multi-Dice, Best of Five) 🎲
# Each player rolls a D6 and a D12
# Highest total wins the round
# Best of 5 rounds determines the champion

import copy
import random
import dice_collection  # make sure dice_collection.py is in the same folder

print("🎲 Welcome to Battle of Dices! 🎲")

# dictionary template for storing player information:
player_info = {
    "name": "",
    "email": "",
    "country": "",
    "wins": 0,
    "rolls": []  # keeps history of [D6, D12, total]
}

# list to store the dicts for each player:
players = []

# obtain the number of players:
number_of_players = int(input("How many players? "))

# for loop to obtain the player info:
for i in range(number_of_players):
    player = copy.deepcopy(player_info)
    player["name"] = input(f"What is the name of player {i + 1}? ")
    player["email"] = input(f"What is the email of player {i + 1}? ")
    player["country"] = input(f"What is the country of player {i + 1}? ")
    players.append(player)

# main game loop (best of 5 rounds)
rounds_played = 0
total_rounds = 5

while rounds_played < total_rounds:
    rounds_played += 1
    input(f"\nRound {rounds_played} - press ENTER to roll the dice...")

    round_results = []  # [name, total_roll]

    for each_player in players:
        roll_d6 = dice_collection.D6()
        roll_d12 = dice_collection.D12()
        total = roll_d6 + roll_d12

        # record the rolls in history
        each_player["rolls"].append((roll_d6, roll_d12, total))

        print(
            f"{each_player['name']} rolled a D6: {roll_d6}, D12: {roll_d12} (total = {total})")
        round_results.append([each_player["name"], total])

    # determine highest total
    max_total = max(result[1] for result in round_results)

    winners = [result[0] for result in round_results if result[1] == max_total]

    # update wins
    if len(winners) == 1:
        for each_player in players:
            if each_player["name"] == winners[0]:
                each_player["wins"] += 1
        print(f"{winners[0]} wins this round!")
    else:
        print("This round is a tie!")

    # show scoreboard
    print("\n Current Scoreboard:")
    for each_player in players:
        print(f"{each_player['name']}: {each_player['wins']} wins")

# determine overall champion(s)
max_wins = max(each_player["wins"] for each_player in players)
champions = [p["name"] for p in players if p["wins"] == max_wins]

print("\n Final Result:")
if len(champions) == 1:
    print(f"{champions[0]} is the Battle of Dices Champion!")
else:
    print("It's a tie between: " + ", ".join(champions))

print(f"\nThe battle lasted {rounds_played} rounds.")

# save results to file
filename = input("Enter the filename to save the results: ")
with open(filename, "w") as file:
    # player information:
    file.write("Player Information:\n\n")
    for each_player in players:
        file.write(
            f"Name: {each_player['name']}\n"
            f"Email: {each_player['email']}\n"
            f"Country: {each_player['country']}\n"
            f"Wins: {each_player['wins']}\n\n"
        )

    file.write("\nGame Rounds:\n")
    for r in range(rounds_played):
        rolls_str = ""
        for i, each_player in enumerate(players):
            d6, d12, total = each_player["rolls"][r]
            rolls_str += f"{each_player['name']} rolled D6={d6}, D12={d12}, Total={total}"
            if i < len(players) - 1:
                rolls_str += " | "
        file.write(f"Round {r+1}: {rolls_str}\n")

print("\n Game over! Results saved successfully.")
