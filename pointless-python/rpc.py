#!/usr/bin/env python3
#Rock Paper Scissors

import os, random

def clear():
    os.system("cls" if os.name=='nt' else "clear")

def scores_table(cpu, player):
    print("+--------+--------+")
    print("|Computer| Player |")
    print("+--------+--------+")

    if cpu < 10 and player < 10:
        print("|   0"+str(cpu)+"   |   0"+str(player)+"   |")
        print("+--------+--------+")
    elif cpu > 10 and player < 10:
        print("|   "+str(cpu)+"   |   0"+str(player)+"   |")
        print("+--------+--------+")
    elif cpu < 10 and player > 10:
        print("|   0"+str(cpu)+"   |   "+str(player)+"   |")
        print("+--------+--------+")
    else:
        print("|   "+str(cpu)+"   |   "+str(player)+"   |")
        print("+--------+--------+")


def game():
    def pick(some_input):
        if some_input == 1:
            return "rock"
        elif some_input == 2:
            return "paper"
        else:
            return "scissors"

    def who_won(cpu, user):
        if cpu == user:
            return "Draw!"
        elif cpu == "rock":
            if user != "paper":
                return "cpu"
            else:
                return "user"
        elif cpu == "paper":
            if user != "scissors":
                return "cpu"
            else:
                return "user"
        elif cpu == "scissors":
            if user != "rock":
                return "cpu"
            else:
                return "user"


    cpu_input = pick(random.randint(1, 3))
    user_input = pick(int(input("\nPlease Choose:\n   [1] - Rock\n   [2] - Paper\n   [3] - Scissors\n")))
    
    return who_won(cpu_input, user_input)

def main(firstrun, cpu_score, user_score):
    clear()
    if firstrun!= True:
        scores_table(cpu_score, user_score)
        winner = game()

        if winner != "Draw!":
            if winner == "cpu":
                cpu_score += 1
            else: 
                user_score +=1
        main(False, cpu_score, user_score)        

cpu_score = 0
user_score = 0
main(False, cpu_score, user_score)