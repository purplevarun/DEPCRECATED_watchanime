# -h for help
# -n for name

import requests
from bs4 import BeautifulSoup
from importlib import import_module
import colors
def showHelp():
    print (colors.Green + "Welcome to purpleanime CLI")
    print (colors.Yellow + "Instructions :")
    print ("1) For help, use -h")
    print ("2) To specify anime, use -n")
    print (colors.Blue + "Example : purpleanime -n attack on titan")
    print (colors.White, end="")

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
        NAME = input(colors.Green + "Enter Name of Anime : " + colors.White)

    # now we have the name of the anime

    AnimeResults = getAnimeList(NAME)
    numOfAnimeResults = len (AnimeResults)
    print ('there were {} results'.format(numOfAnimeResults))
    print (AnimeResults)

if __name__ == '__main__': onigiri()