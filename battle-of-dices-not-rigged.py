

import dice_collection


print("🎲 Welcome to Battle of Dices! 🎲")

# Variables to keep track of the score:
player1_wins = 0
player2_wins = 0
rounds_played = 0

list_of_player1_roll = []
list_of_player2_roll = []

while (player1_wins < 3 and player2_wins < 3):

    rounds_played += 1
    # Round 1
    input("\nPress ENTER to roll the dice...")
    player1_roll = dice_collection.D6()
    print("Player 1 rolled: ",  player1_roll)
    list_of_player1_roll.append(player1_roll)

    player2_roll = dice_collection.D6()
    print("Player 2 rolled: ", player2_roll)
    list_of_player2_roll.append(player2_roll)

    input("\nPress ENTER to continue...")

    # So far so good right? But how to check who got the highest roll?

    if player1_roll > player2_roll:
        player1_wins += 1
        print("Player 1 wins this round!")
        print("Because ", player1_roll,
              " is greater than ", player2_roll)
        winner = "the winner is player 1"

    elif player1_roll < player2_roll:
        player2_wins += 1
        print("Player 2 wins this round!")
        print("Because ", player2_roll,
              " is greater than ", player1_roll)
        winner = "the winner is player 2"
    else:
        print("Amaaazzinng! This round has a tie!")
        winner = "tie"

    # We can print the game score:
    print("The game score is Player1 ", player1_wins,
          " vs. ", player2_wins, " Player 2.")

    # Now we need to check if either player won.
    if player1_wins == 3:
        print("Player 1 is the newest Battle of Dices Champion! ")

    elif player2_wins == 3:
        print("Player 2 is the newest Battle of Dices Champion! ")
    else:
        print("This heated Battle of Dices is still going on! Who will win in the end? ")
        winner = "tie"

    print(winner)
    # Since none of them would have won after 1 round, we could copy this code several times
    # until we have enough times to make sure someone wins.
print(f"the number of rounds completed is: {rounds_played}")


filename = input("Enter the filename to save the results:")

with open(filename, "w") as file:
    for i in range(len(list_of_player1_roll)):
        file.write(
            f"Round {i+1}: player 1 rolled {list_of_player1_roll[i], }, player 2 rolled {list_of_player2_roll[i], }")
