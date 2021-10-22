# -h for help
# -n for name

import requests
from bs4 import BeautifulSoup

RedColor     = "\033[1;31m"
GreenColor   = "\033[1;32m"
YellowColor  = "\033[1;33m"
BlueColor    = "\033[1;34m"
WhiteColor   = "\u001b[37m"
def showHelp():
    print (GreenColor + "Welcome to purpleanime CLI")
    print (YellowColor + "Instructions :")
    print ("1) For help, use -h")
    print ("2) To specify anime, use -n")
    print (BlueColor + "Example : purpleanime -n attack on titan")
    print (WhiteColor, end="")

def extractName(args):
    name = ""
    start = False
    for i in args:
        if i == '-n' :
            start = True
            continue
        if start :
            name = name + i + " "
    return name

def getAnimeList (NAME):
    NAME = NAME.rstrip()
    NAME = NAME.lstrip()
    NAME = NAME.replace(" ", "%20")
    searchUrl = "https://gogoanime.vc//search.html?keyword={}".format(NAME)
    searchResponse = requests.get(searchUrl)
    soup = BeautifulSoup (searchResponse.content, 'html5lib')
    namesInHTML = soup.findAll("p", class_="name")
    Animes = []
    for i in namesInHTML:
        x = i.find("a")
        title = x.get('title')
        Animes.append(title)
    return Animes
    
def onigiri ():
    import sys
    arguments = sys.argv
    numOfArguments = len (sys.argv) - 1
    filename = arguments[0]
    arguments = arguments[1:]
    NAME = None

    if "-h" in arguments:
        showHelp()
        exit(-1)

    if "-n" in arguments:
        NAME = extractName(arguments)
    else :
        NAME = input(GreenColor + "Enter Name of Anime : " + WhiteColor)

    # now we have the name of the anime

    AnimeResults = getAnimeList(NAME)
    numOfAnimeResults = len (AnimeResults)
    

if __name__ == '__main__': onigiri()