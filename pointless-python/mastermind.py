#!/usr/bin/python3
#Mastermind
import random

s = ["1", "2", "3", "4"]

def main(s):
    count = 1
    
    print("---MASTERMIND---\n")
    print("Guess the numbers in as few tries as possible.\nOnly use numbers 1 to 4 and use 4 didgets.")
    
    numbers = ""
    for i in range (1, 5):
        numbers = numbers + random.choice(s)

    cpuarray = list(numbers)
    game(count, cpuarray)
    

def game(count, cpuarray):
    userguess = input(str(count)+">")
    userarray = list(userguess)

    output = ""
    for i in range (0, 4):
        if userarray[i] == cpuarray[i]:
            output += "*"

    print(output + "\n")
    
    if output == "****":
        print("Well Done. It Took you " + str(count) + " Attempts")
        again = input("Type 'retry' to try again or press enter to end.")
        if again == "retry":
            main(s)
    else:
        count += 1
        game(count, cpuarray)
        
        
    

main(s)
