#!/usr/bin/env python3
#Rock Paper Scissors - The New Version

import random, os, time, sys

def clear():
    os.system('cls' if os.name == 'nt' else "clear")

def make_dict():
    rock = dict({"beats": "Scissors", "beaten_by": "Paper"})
    paper = dict({"beats": "Rock", "beaten_by": "Scissors"})
    scissors = dict({"beats": "Paper", "beaten_by": "Rock"})

    beats = dict({"rock": rock, "paper": paper, "scissors": scissors})
    options = dict({"1": "Rock", "2": "Paper", "3": "Scissors"})

    return beats, options

def scores(player=0, cpu=0, player2=None):
    if player2 == None:
        return "CPU = " + str(cpu) + "\nPlayer = " + str(player)
    else:
        return "Player 1 = " + str(player) + "\nPlayer 2 = " + str(player2)

def game(check_scores, options, player_score, cpu_score, player2_score=None):
    clear()
    if player2_score == None:
        print(scores(player=player_score, cpu=cpu_score))
        cpu_input = options[str(random.randint(1, 3))]
        try:
            player_input = options[str(int(input("\nPlease Choose an Option (1, 2, 3):\n1: Rock\n2: Paper\n3: Scissors\n\nYour Choice: ")))]
        except:
            clear()
            print("Invalid Pick")

            sys.stdout.write("\rPlease Wait 1 Second")
            sys.stdout.flush()
            time.sleep(1)
            sys.stdout.write("\rPlease Wait 0 Seconds")
            sys.stdout.flush()
            time.sleep(1)
            game(check_scores, options, player_score, cpu_score)

        if cpu_input == player_input:
            clear()
            print("Draw!")
            print("You Picked: " + str(player_input))
            print("CPU Picked: " + str(cpu_input))

        else:
            if player_input == check_scores[cpu_input.lower()]["beaten_by"]:
                clear()
                print("Player Wins!")
                print("Player Picked: " + str(player_input))
                print("CPU Picked: " + str(cpu_input)) 
                player_score += 1
            else:
                clear()
                print("CPU Wins!")
                print("Player Picked: " + str(player_input))
                print("CPU Picked: " + str(cpu_input)) 
                cpu_score += 1
        

        sys.stdout.write("\rPlease Wait 1 Second")
        sys.stdout.flush()
        time.sleep(1)
        sys.stdout.write("\rPlease Wait 0 Seconds")
        sys.stdout.flush()
        time.sleep(1)
        game(check_scores, options, player_score, cpu_score)
    else:
        print(scores(player=player_score, player2=player2_score))
        try:
            player1_input = options[str(int(input("\nPlayer 1 Please Choose an Option (1, 2, 3):\n1: Rock\n2: Paper\n3: Scissors\n\nYour Choice: ")))]
            clear()
            player2_input = options[str(int(input("\nPlayer 2 Please Choose an Option (1, 2, 3):\n1: Rock\n2: Paper\n3: Scissors\n\nYour Choice: ")))]
        except:
            clear()
            print("Invalid Pick")

            sys.stdout.write("\rPlease Wait 1 Second")
            sys.stdout.flush()
            time.sleep(1)
            sys.stdout.write("\rPlease Wait 0 Seconds")
            sys.stdout.flush()
            time.sleep(1)
            game(check_scores, options, player_score, None, player2_score)

        if player1_input == player2_input:
            clear()
            print("Draw!")
            print("Player 1 Picked: " + str(player1_input))
            print("Player 2 Picked: " + str(player2_input))

        else:
            if player1_input == check_scores[player2_input.lower()]["beaten_by"]:
                clear()
                print("Player 1 Wins!")
                print("Player 1 Picked: " + str(player1_input))
                print("Player 2 Picked: " + str(player2_input)) 
                player_score += 1
            else:
                clear()
                print("Player 2 Wins!")
                print("Player 1 Picked: " + str(player1_input))
                print("Player 2 Picked: " + str(player2_input)) 
                player2_score += 1
                

        sys.stdout.write("\rPlease Wait 1 Second")
        sys.stdout.flush()
        time.sleep(1)
        sys.stdout.write("\rPlease Wait 0 Seconds")
        sys.stdout.flush()
        time.sleep(1)
        game(check_scores, options, player_score, None, player2_score)

def setup():
    check_score, options = make_dict()
    clear()
    print("This is a Development Version of the RPS Application")
    print("Please Press CTRL+Z to Exit\n")
    players = int(input("Please Pick an Option:\n1: One Player\n2: Two Player\n\nYour Choice: "))
    if players == 1:
        game(check_score, options, 0, 0)
    elif players == 2:
        game(check_score, options, 0, 0, 0)
    else:
        setup()


setup()