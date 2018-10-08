#!/usr/bin/env python3

#Longest Availiable Word using a 7-Segment Display. 
#Inspired by https://youtu.be/zp4BMR88260 by Tom Scott

#This program will NOT work on Windows or any Unix-Like Operating System without the Hunspell Dictionary.
#This program will be availiable for those OSs at a later date.

import os, re

if os.name != "posix":
    print("This program will not work on %s. Please Use Ubuntu or another Unix-Like operating system with the hunspell dictionary.")

#Initiate the List
acceptable_words = []

#Regex Expression - gkmqvwxz because they are impossible to make, ios becasue they are reused by l. ' because it cannot be represented.
regex_pattern = r'[gioksmqvwxz\']'

#Set the initial length to 0
longest_len = 0

#Sort the Words
with open("/usr/share/hunspell/en_US.dic", "r") as f:
    #For each Line in file. - line is a python keyword for this.
    for line in f:
        #Take out any characters which shouldn't be there and convert to lower case.
        word = f.readline().split("/")[0].split("\n")[0].lower()
        #Apply the regular expression, and expect None due to no matches. 
        if re.search(regex_pattern, word) == None:
            #Add it to the list
            acceptable_words.append(word)
            #Check the word length and compare to previous longest
            if len(word) > longest_len:
                #If true, increase the length of the longest.
                longest_len = len(word)

#All words matching longest_len list
longest_words = []

#For each word which matches regex, find the longest ones.
for word in acceptable_words:
    if len(word) == longest_len:
        longest_words.append(word)

#print it out
print(longest_words)