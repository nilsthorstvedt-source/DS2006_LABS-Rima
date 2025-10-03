
# Battle of Dices is going to be an amazing 2 player game,
# where two players face each other using only their sheer luck!
#
# The rules are:
#
# Each player throws one D6.
# The player with the highest roll wins the round.
# The first player to win 3 times is the winner.
#
# Our main task today is to implement the code necessary to bring this
# amazing game alive!

import random

print("🎲 Welcome to Battle of Dices! 🎲")

# Variables to keep track of the score:
player1_wins = 0
player2_wins = 0

player1_round1_roll = 0
player1_round2_roll = 0
player1_round3_roll = 0
player1_round4_roll = 0
player1_round5_roll = 0

player2_round1_roll = 0
player2_round2_roll = 0
player2_round3_roll = 0
player2_round4_roll = 0
player2_round5_roll = 0

# variables to save result
winner = None

# Round 1
input("\nPress ENTER to roll the dice...")

player1_roll = random.randint(1, 100)
print("Player 1 rolled: ",  player1_roll)
player1_round1_roll = player1_roll

player2_roll = random.randint(1, 100)
print("Player 2 rolled: ", player2_roll)
player2_round1_roll = player2_roll

input("\nPress ENTER to continue...")


# So far so good right? But how to check who got the highest roll?

if player1_roll > player2_roll:
    player1_wins += 1
    print("Player 1 wins this round!")
    print("Because ", player1_roll, " is greater than ", player2_roll)
    winner = player1_wins

elif player1_roll < player2_roll:
    player2_wins += 1
    print("Player 2 wins this round!")
    print("Because ", player2_roll, " is greater than ", player1_roll)
    winner = player2_wins
else:
    print("Amaaazzinng! This round has a tie!")

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

print(winner)
# Since none of them would have won after 1 round, we could copy this code several times
# until we have enough times to make sure someone wins.


# Round 2
input("\nPress ENTER to roll the dice...")

player1_roll = random.randint(1, 100)
print("Player 1 rolled: ",  player1_roll)
player1_round2_roll = player1_roll

player2_roll = random.randint(1, 100)
print("Player 2 rolled: ", player2_roll)
player2_round2_roll = player2_roll

input("\nPress ENTER to continue...")


# So far so good right? But how to check who got the highest roll?

if player1_roll > player2_roll:
    player1_wins += 1
    print("Player 1 wins this round!")
    print("Because ", player1_roll, " is greater than ", player2_roll)
    winner = player1_wins

elif player1_roll < player2_roll:
    player2_wins += 1
    print("Player 2 wins this round!")
    print("Because ", player2_roll, " is greater than ", player1_roll)
    winner = player2_wins
else:
    print("Amaaazzinng! This round has a tie!")

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

print(winner)
# Since none of them would have won after 1 round, we could copy this code several times
# until we have enough times to make sure someone wins.


# Round 3
input("\nPress ENTER to roll the dice...")

player1_roll = random.randint(1, 100)
print("Player 1 rolled: ",  player1_roll)
player1_round3_roll = player1_roll

player2_roll = random.randint(1, 100)
print("Player 2 rolled: ", player2_roll)
player2_round3_roll = player2_roll

input("\nPress ENTER to continue...")


# So far so good right? But how to check who got the highest roll?

if player1_roll > player2_roll:
    player1_wins += 1
    print("Player 1 wins this round!")
    print("Because ", player1_roll, " is greater than ", player2_roll)
    winner = player1_wins

elif player1_roll < player2_roll:
    player2_wins += 1
    print("Player 2 wins this round!")
    print("Because ", player2_roll, " is greater than ", player1_roll)
    winner = player2_wins
else:
    print("Amaaazzinng! This round has a tie!")

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


if (player1_wins < 3 and player2_wins < 3):

  # Round 4
    input("\nPress ENTER to roll the dice...")

    player1_roll = random.randint(1, 100)
    print("Player 1 rolled: ",  player1_roll)
    player1_round4_roll = player1_roll

    player2_roll = random.randint(1, 100)
    print("Player 2 rolled: ", player2_roll)
    player2_round4_roll = player2_roll

    input("\nPress ENTER to continue...")

    # So far so good right? But how to check who got the highest roll?

    if player1_roll > player2_roll:
        player1_wins += 1
        print("Player 1 wins this round!")
        print("Because ", player1_roll, " is greater than ", player2_roll)
        winner = player1_wins

    elif player1_roll < player2_roll:
        player2_wins += 1
        print("Player 2 wins this round!")
        print("Because ", player2_roll, " is greater than ", player1_roll)
        winner = player2_wins
    else:
        print("Amaaazzinng! This round has a tie!")

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

if (player1_wins < 3 and player2_wins < 3):
    # Round 5
    input("\nPress ENTER to roll the dice...")

    player1_roll = random.randint(1, 100)
    print("Player 1 rolled: ",  player1_roll)
    player1_round5_roll = player1_roll

    player2_roll = random.randint(1, 100)
    print("Player 2 rolled: ", player2_roll)
    player2_round5_roll = player2_roll

    input("\nPress ENTER to continue...")

    # So far so good right? But how to check who got the highest roll?

    if player1_roll > player2_roll:
        player1_wins += 1
        print("Player 1 wins this round!")
        print("Because ", player1_roll, " is greater than ", player2_roll)
        winner = player1_wins

    elif player1_roll < player2_roll:
        player2_wins += 1
        print("Player 2 wins this round!")
        print("Because ", player2_roll, " is greater than ", player1_roll)
        winner = player2_wins
    else:
        print("Amaaazzinng! This round has a tie!")

    # We can print the game score:
    print("The game score is Player1 ", player1_wins,
          " vs. ", player2_wins, " Player 2.")

    # Now we need to check if either player won.
    if player1_wins == 3:
        print("Player 1 is the newest Battle of Dices Champion! ")

    elif player2_wins == 3:
        print("Player 2 is the newest Battle of Dices Champion! ")
    else:
        print("too bad, no one wins ")

print("Round    | 1 | 2 | 3 | 4 | 5 |")
print(f"Player1 |{player1_round1_roll} | {player1_round2_roll} | {player1_round3_roll} | {player1_round4_roll} | {player1_round5_roll} |")
print(f"Player2 |{player2_round1_roll} | {player2_round2_roll} | {player2_round3_roll} | {player2_round4_roll} | {player2_round5_roll} |")
