# -h for help
# -n for name

import requests
from bs4 import BeautifulSoup
import colors, extract
def showHelp():
    print (colors.Green + "Welcome to purpleanime CLI")
    print (colors.Yellow + "Instructions :")
    print ("1) For help, use -h")
    print ("2) To specify anime, use -n")
    print (colors.Blue + "Example : purpleanime -n attack on titan")
    print (colors.White, end="")
    
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
        NAME = extract.extractName(arguments)
    else :
        NAME = input(colors.Green + "Enter Name of Anime : " + colors.White)

    # now we have the name of the anime

    AnimeResults = extract.getAnimeList(NAME)
    numOfAnimeResults = len (AnimeResults)
    if (numOfAnimeResults == 0) : 
        print (colors.Red+'There are {} results for your search'.format(numOfAnimeResults))
        exit (-1)
    dp = extract.getIndexDict(AnimeResults)
    for i, j in dp.items():
        print (colors.Yellow + str(i) + " " + colors.Green + j + colors.White)
    try :
        query = int (input (colors.Blue + "Choose Anime : " + colors.White))
    except:
        print (colors.Red + "Please choose the index of the Anime"); exit(-1)
    
    selectedAnime = dp[query]

    startEp, endEp = extract.getEpCountOfSelectedAnime(selectedAnime)

    try :
        selectedEpisode = int (input (colors.Magenta + 'Select episode number between 1 and {} : '.format(endEp) + colors.White))
    except:
        print (colors.Red + "Episode Number has to be a NUMBER" + colors.White); exit(-1)
    
    videoLink = extract.getLink(selectedAnime, selectedEpisode)
if __name__ == '__main__': onigiri()