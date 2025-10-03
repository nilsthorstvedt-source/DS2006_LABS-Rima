# 🎲 Battle of Dices (Nested Lists, Multi-Dice, Best of Five) 🎲
# Each player rolls a D6 and a D12
# Highest total wins the round
# Best of 5 rounds determines the champion

import dice_collection

print("🎲 Welcome to Battle of Dices! 🎲")


# Get number of players and their names

num_players = int(input("Enter the number of players: "))

players = []  # [name, score]
for i in range(num_players):
    name = input(f"Enter name for Player {i+1}: ")
    players.append([name, 0])  # score starts at 0


# Main game loop (best of 5 rounds)

rounds_played = 0
total_rounds = 5

while rounds_played < total_rounds:
    rounds_played += 1
    input(f"\n Round {rounds_played} - press ENTER to roll the dice...")

    round_results = []  # [name, total_roll]

    # Each player rolls two dice (D6 + D12)
    for i in range(len(players)):
        name = players[i][0]
        total = 0

        dice_roll_d6 = dice_collection.D6()

        total += dice_roll_d6
        print(f"{name} rolled a D6: {dice_roll_d6}")

        dice_roll_d12 = dice_collection.D12()
        total += dice_roll_d12
        print(f"{name} rolled a D12: {dice_roll_d12}")

        round_results.append([name, total])
        print(f"{name}'s total: {total}")

    # Find highest total

    max_total = 0
    for result in round_results:
        if result[1] > max_total:
            max_total = result[1]

    winners = []
    for result in round_results:
        if result[1] == max_total:
            winners.append(result[0])

    # Update scores

    if len(winners) == 1:
        for player in players:
            if player[0] == winners[0]:
                player[1] += 1
        print(f"{winners[0]} wins this round!")
    else:
        print("This round is a tie!")

    # Show scoreboard
    print("\n Current Scoreboard:")
    for player in players:
        print(f"{player[0]}: {player[1]}")


# Determine overall champion
max_score = 0
champions = []
for player in players:
    if player[1] > max_score:
        max_score = player[1]

for player in players:
    if player[1] == max_score:
        champions.append(player[0])

# Print the result
if len(champions) == 1:
    print(f"\n {champions[0]} is the Battle of Dices Champion!")
else:
    print("\n It's a tie between: ", end="")
    for i, name in enumerate(champions):
        if i != 0:
            print(", ", end="")  # print comma before all except first
        print(name, end="")
    print()  # add newline at the end

print(f"\nThe battle lasted {rounds_played} rounds.")
