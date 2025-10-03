# 🎲 Battle of Dices (Nested Lists, Loops Only) 🎲
# Rules:
# - Each player rolls a D6
# - Highest roll wins the round
# - First player to win 3 rounds is the Champion

import dice_collection

print("🎲 Welcome to Battle of Dices! 🎲")


# Get number of players and their names
num_players = int(input("Enter the number of players: "))

players = []  # nested list: [name, score]
for i in range(num_players):
    name = input(f"Enter name for Player {i+1}: ")
    players.append([name, 0])   # everyone starts with score 0


# Initialize player rolls (empty list for each player)
player_rolls = []
for i in range(num_players):
    player_rolls.append([])


# Main game loop
rounds_played = 0
rounds_to_win = 3
champion_found = False  # flag to break out of the loop

while not champion_found:
    rounds_played += 1
    input(f"\n Round {rounds_played} - press ENTER to roll the dice...")

    round_results = []  # store [name, roll] for this round

    # Each player rolls
    for i in range(len(players)):
        name = players[i][0]
        dice_roll = dice_collection.D6()
        player_rolls[i].append(dice_roll)  # save roll history
        round_results.append([name, dice_roll])
        print(f"{name} rolled: {dice_roll}")

    # Find highest roll
    max_roll = 0
    for result in round_results:
        if result[1] > max_roll:
            max_roll = result[1]

    # Find all winners
    winners = []
    for result in round_results:
        if result[1] == max_roll:
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

    # Check if someone reached 3 wins
    for player in players:
        if player[1] >= rounds_to_win:
            print(f"\n {player[0]} is the newest Battle of Dices Champion!")
            champion_found = True  # stop the game immediately
            break  # exit the loop checking players

print(f"\nThe battle lasted {rounds_played} rounds.")
