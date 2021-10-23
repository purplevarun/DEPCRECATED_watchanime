# -h for help
# -n for name
import colors, extract
import os, sys
player = "mpv.exe"
def showHelp():
    print ("Welcome to purpleanime CLI")
    print ("Instructions :")
    print ("1) For help, use -h")
    print ("2) To specify anime, use -n")
    print ("Example : purpleanime -n attack on titan")
    
    
def onigiri ():
    arguments = sys.argv
    numOfArguments = len (sys.argv) - 1
    filename = arguments[0]
    arguments = arguments[1:]
    NAME = None
    QUALITY = 720
    if "-h" in arguments:
        showHelp()
        exit(-1)

    if "-n" in arguments:
        NAME = extract.extractName(arguments)
    else :
        NAME = input("Enter Name of Anime : " )

    # now we have the name of the anime

    AnimeResults = extract.getAnimeList(NAME)
    numOfAnimeResults = len (AnimeResults)
    if (numOfAnimeResults == 0) : 
        print ('There are {} results for your search'.format(numOfAnimeResults))
        exit (-1)
    dp = extract.getIndexDict(AnimeResults)
    for i, j in dp.items():
        print (str(i) + " "+ j)
    try :
        query = int (input ("Choose Anime : "))
    except:
        print ("Please choose the index of the Anime"); exit(-1)
    
    selectedAnime = dp[query]

    startEp, endEp = extract.getEpCountOfSelectedAnime(selectedAnime)

    try :
        selectedEpisode = int (input ('Select episode number between 1 and {} : '.format(endEp)))
    except:
        print ("Episode Number has to be a NUMBER"); exit(-1)
    
    embeddedLink = extract.getLink(selectedAnime, selectedEpisode)
    videoLink = extract.getVideoLink (embeddedLink, QUALITY)
    
    command = '{} --http-header-fields="Referer: {}" "{}"'.format(player,embeddedLink,videoLink)
    os.system(command)
    
if __name__ == '__main__': onigiri()