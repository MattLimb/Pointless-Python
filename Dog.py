#!/usr/bin/python3

from bs4 import BeautifulSoup
from urllib import request
import webbrowser
import os

def clear():
    os.system('cls' if os.name=='nt' else 'clear')

def get_dog(url, folder, allimages):
    html = request.urlopen(url + folder).read()
    soup = BeautifulSoup(html, "lxml")
    dog = soup.find("body").string
    
    image = url + dog
    allimages.append(image)
    webbrowser.open_new(image)
    clear()
    
def get_dog_second(url, folder, allimages):
    for x in range(1, 6):
        realurl = url + folder
        html = request.urlopen(realurl).read()
        soup = BeautifulSoup(html, "lxml")
        dog = soup.find("body").string

        image = url + dog
        allimages.append(image)
        clear()

    for x in allimages:
        webbrowser.open_new_tab(x)
        print(x)

    
    
target_url = "https://random.dog/"
target_folder = "woof/" 
firstrun = True
stop = False



while stop == False:
    if firstrun == True:
        yn = input("Do you want to see a dog?\n")
        if (yn == "y") or (yn == "Y"):
            firstrun = False
            all_images = []
            get_dog_second(target_url, target_folder, all_images)
            #clear()
        else:
            stop = True
            #clear()
    elif firstrun == False:
        yn = input("Do you want to see another dog?\n")
        if (yn == "y") or (yn == "Y"):
            firstrun = False
            all_images = []
            get_dog_second(target_url, target_folder, all_images)
            #clear()
        else:
            #clear()
            stop = True


            
