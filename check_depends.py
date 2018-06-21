#!/usr/bin/python3

import os, subprocess

def main(*args):
    for x in args:
        try:
            print("Checking " + str(x) + "...")
            __import__(x)
        except ModuleNotFoundError:
            command = "sudo pip3 install " + str(x)
            subprocess.Popen(command, shell=True, executable='/bin/bash').wait()



if os.name == "posix":
    f = open(".depends/depends.txt", "r")
    dep = f.readlines()
    f.close()
    for x in dep:
        main(x.strip("\n"))
    
else:
    print("I cannot run on " + os.name + ". Sorry!")