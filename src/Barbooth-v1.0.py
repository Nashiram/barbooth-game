# Barbooth 1.0 by Ano
# Copyright © 2018 Andrei Onea

# This game is probably illegal in some places but that does not matter
# as this is only a personal project. It takes two player names, rolls
# two random dices and prints out the winner. There are two game modes:
# "highs" designates the highst dice as the winner; "lows" viceversa.
# The game features a round counter and a decent user interface. Future
# plans include adding a log file in an user-chosen folder which stores
# a short history of recent games, creating a 'history' command to fetch
# that information and creating executable files for each Operating System. 
# This is a personal project so please do not expect much for it. 
# Any issues you have, you can contact me on the moon.
 
# Importing dependencies
import random
import time

# Game core. It runs when user executes 'play' cmd. 
# Takes the names of the players as its arguments
# It is controlled by the gameController
def play(nameP1, nameP2):    

    # variable used to indicate the state of the game: 0: game not over
    #                                                  1: game is over                                        
    gameover = 0

    # round counter
    round = 1

    # scores counter
    scoreP1 = 0
    scoreP2 = 0

    # Main game loop. It exists when the user runs the mm command
    # or when a round finishes and there is no desire to stat another one
    while gameover == 0:

        # Rolling dices and assigning the values to diceP1 and diceP2
        diceP1 = random.randint(1,6)
        diceP2 = random.randint(1,6)

        # States the state of the current round: 0: round not over
        #                                        1: round is over
        roundover = 0

        # Printing the round counter
        print("\n####################### Round " + str(round) + " #######################")

        # Initialization of the little brain of the game
        # i.e takes inputs from the user and controlls the flow of the game
        gameController = input("\nHighs or lows?  >  ")

        # Check if the input is not the 'mm' cmd
        if gameController == "mm":
            break

        # Otherwise, gameController checks user inputs until the round is over
        else:
            while roundover != 1:

                # Controlling "highs" choice
                if gameController == "highs" or gameController == "Highs" or gameController == "h":

                    # Print to the user interface
                    print("Rolling dices...")

                    # Creates a small delay in order to give the effect of the waiting for the dices to stop rolling
                    time.sleep(random.randint(1,2))

                    # Prints what each player "rolled"
                    print("\n" + nameP1 + " rolled " + str(diceP1) + "!")
                    print(nameP2 + " rolled " + str(diceP2) + "!")

                    # Compares the dices and selects the winner (or says it is a draw), printing a message on the user interface, while updating the score
                    if diceP1 > diceP2:
                        print(nameP1 + " won!")
                        scoreP1 += 1
                    elif diceP1 == diceP2:
                        print("It's a draw!")
                    else:
                        print(nameP2 + " won!")
                        scoreP2 += 1
                    roundover = 1

                # Controlling "lows" choice
                elif gameController == "lows" or gameController == "Lows" or gameController == "l":

                    # Print to the user interface
                    print("Rolling dices...")

                    # Creates a small delay in order to give the effect of the waiting for the dices to stop rolling
                    time.sleep(random.randint(1,2))

                    # Prints what each player "rolled"
                    print("\n" + nameP1 + " rolled " + str(diceP1) + "!")
                    print(nameP2 + " rolled " + str(diceP2) + "!")

                    # Compares the dices and selects the winner (or says it is a draw), printing a message on the user interface, while updating the score
                    if diceP1 < diceP2:
                        print(nameP1 + " won!")
                        scoreP1 += 1
                    elif diceP1 == diceP2:
                        print("It's a draw!")
                    else:
                        print(nameP2 + " won!")
                        scoreP2 += 1
                    roundover = 1

                # Checks if the user wants to go back to the main menu
                elif gameController == "mm":
                    break

                # If input is wrong, asks player to try again a valid choice
                else:
                    gameController = input("Please enter a valid choice: highs or lows?  >  ")

            # end while
        # end if else

        # Ensures the game is exited when the 'mm' cmd is executed in the previous round loop
        if gameController == "mm":
            break

        # After a round, prints the current score
        print("Score: " + nameP1 + " " + str(scoreP1) + " - " + str(scoreP2) + " " + nameP2)

        # The game is now over unless another round is specified by the user
        gameover = 1

        # Asks the player whether he/she wants to play again or not
        playAgain = input("\nPlay again? (y/n)  >  ")

        # Loops until a valid choice is given or the 'mm' cmd is issued
        while playAgain != "mm":

            # If yes, set the flag such that game is not over and start another round updating the previous score
            if playAgain == "y":
                gameover = 0
                round += 1
                break
            # end if

            # If no, compare the final scores and congratulate the winner, or say if it is a draw
            elif playAgain == "n":
                print("\nFinal score: " + nameP1 + " " + str(scoreP1) + " - " + str(scoreP2) + " " + nameP2)
                if scoreP1 > scoreP2:
                    print("$$$ " + nameP1 + " won! $$$\n")
                elif scoreP1 == scoreP2:
                    print("It's a draw :(")
                else:
                    print("$$$ " + nameP2 + " won! $$$\n")
                break
            # end elif
            
            # Catches any another faul input
            else:
                playAgain = input("Please enter `y` for yes, and `n` for no  >  ")
        # end while
    # end while
#end play

#DEFAULT MESSAGE. GETS PRINTED ONCE WHEN STARTING THE PROGRAM
print("========================================")                               
print("====      Barbooth 1.0 by Ano       ====")
print("====  Copyright © 2018 Andrei Onea  ====")
print("========================================")
print("Tip: Use `help` for a list of useful commands")
print("----------------------------------------")
print("\n")

# The big brain. In other words, unlike gameController, appController
# controls the outer aspect of the application, giving the user access
# to start/quit a game or find information about the game and the author
appController = input("[Main Menu] ~ Please enter your command  >  ")

# Checks if the cmd given is the 'quit' app one. Otherwise, ask for other commands
while appController != "quit":                                                    

    # If 'play' is issued, then the game is instantiated    
    if appController == "play":

        # When the game loop is entered, announces the game process has been started
        print("[Barbooth] Game initialized\n")

        # Gets the player names from the user
        playerOneName = input("Player one enter your name: ")
        playerTwoName = input("Player two enter your name: ")

        # Instantiates a game with the two given names
        play(playerOneName, playerTwoName)

        # After the game loop is exited, announces the game process has been killed
        print("[Barbooth] Game terminated")

    # Prints the Help page
    elif appController == "help":
        print("\n--------------------------------------- Help (1/1) ---------------------------------------------")
        print("help    displays this text")
        print("about   information about the game and the author")
        print("play    starts a new game")
        print("        intructions will appear on the screen")
        print("mm      returns you to the main menu (can be used anywhere during the game,")
        print("        but don't use it while in main menu...)")
        print("quit    quits the program (use 'mm' if you are currently in a game)")
        print("--------------------------------------- Help (1/1) ---------------------------------------------")

    # If 'mm' is issued, then we have a problem. The appController makes sure to let us know
    elif appController == "mm":
        print("You are already here...")

    # Prints the About page
    elif appController == "about":
        print("\n----------------------------------------- About -----------------------------------------------")
        print("Barbooth is a illegal game. Thus, I, Andrei Onea, made this game in the Maths example class while waiting to get marked. Just for fun and experience. ")
        print("It takes two player names, rolls two random dices and prints out the winner.")
        print("There are two game modes: \"highs\" designates the highst dice as the winner; \"lows\" viceversa.")
    
    # Catches any invalid input, showing a useful tip
    else:
        print("Invalid command. Please use `help` for a list of commands!")
    
    # Ensures the app loop continues
    appController = input("\n[Main Menu] ~ Please enter your command  >  ")                          

# Just an quitting statement
print("[Barbooth] Quitting game...\n")                          

# The application would exit instantly since it is not very resources-dependent
# Thus, it is given another delay for a more natural app closin feeling
time.sleep(random.randint(1,2))
