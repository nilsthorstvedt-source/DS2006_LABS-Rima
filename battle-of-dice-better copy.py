# Battle of Dices is a 2 player game,
# where two players face each other using only their sheer luck!
#
# The rules are:
#
# Each player throws one D6.
# The player with the highest roll wins the round.
# The first player to win 3 times is the winner.


import dice_collection


print("🎲 Welcome to Battle of Dices! 🎲")

# Variables to keep track of the score:
player1_wins = 0
player2_wins = 0
rounds_played = 0

while (player1_wins < 3 and player2_wins < 3):

    rounds_played += 1
    # Round 1
    input("\nPress ENTER to roll the dice...")
    player1_roll = dice_collection.D6()

    print("Player 1 rolled: ",  player1_roll)

    player2_roll = dice_collection.D6()

    print("Player 2 rolled: ", player2_roll)

    input("\nPress ENTER to continue...")

# compare reaults
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
