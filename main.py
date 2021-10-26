from bs4 import BeautifulSoup
import requests, html5lib
import sys, os
from random import randint

RED     = "\u001b[31;1m"
GREEN   = "\u001b[32;1m"
WHITE   = "\u001b[37;1m"
BLUE    = "\u001b[34;1m"
MAGENTA = "\u001b[35;1m"
YELLOW  = "\u001b[33;1m"

def getRandomColor(): # get random color
    colors = [RED, GREEN, BLUE, WHITE, MAGENTA, YELLOW]
    l = len (colors)
    r = randint(0, l-1)
    return colors[r]

def killProgram(): # name not given
    print (RED+'An Error has occured'+WHITE)
    exit (-1)

def getNames(searchText)->list:
    searchText = str(searchText)
    searchText.replace(" ","%20")
    response = requests.get('https://gogoanime.vc//search.html?keyword='+searchText)
    soup =  BeautifulSoup(response.content, 'html5lib')
    soup = soup.findAll("p", class_="name")
    Names = []
    for i in soup:
        x = str(i)
        idx = x.index("/category/")
        x = x[(idx+10):]
        idx = x.index('"')
        Names.append(x[:idx])
    return Names

def getChoice(Names)->str:
    dp = {}
    c = 1
    for i in Names:
        dp[c] = i
        c += 1
    for key, value in dp.items():
        print("{} {}{}{}".format(key,getRandomColor(),value,WHITE))
    try :
        ch = int( input ("Enter Choice - "))
    except:
        killProgram()
    return dp[ch]

def main(): 
    Name = ""
    args = sys.argv
    if len (args) <= 1: killProgram()
    for i in range (1, len(args)):
        Name += args[i] + " "
    #
    Possibilities = getNames(Name)
    #
    choice = getChoice (Possibilities)
if __name__ == '__main__': 
    main()
