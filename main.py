from bs4 import BeautifulSoup
import requests
import os
from random import randint

RED     = "\u001b[31;1m"
GREEN   = "\u001b[32;1m"
WHITE   = "\u001b[37;1m"
BLUE    = "\u001b[34;1m"
MAGENTA = "\u001b[35;1m"
YELLOW  = "\u001b[33;1m"
CYAN    = "\u001b[36;1m"

RED     = ""
GREEN   = ""
WHITE   = ""
BLUE    = ""
MAGENTA = ""
YELLOW  = ""
CYAN    = ""
provider = "https://gogoanome.mc"
def getRandomColor(): # get random color
    colors = [GREEN, BLUE, MAGENTA, YELLOW, CYAN]
    l = len (colors)
    r = randint(0, l-1)
    return colors[r]

def killProgram(): # name not given
    print (RED+'An Error has occured'+WHITE)
    exit (-1)

def getNames(searchText)->list:
    searchText = str(searchText)
    searchText.replace(" ","%20")
    response = requests.get(provider+'//search.html?keyword='+searchText)
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
    if ch <= 0 or ch > len(dp) : killProgram()
    
    return dp[ch]

def getEpisode(Name)->int:
    response = requests.get('{}//category/{}'.format(provider,Name))
    soup = BeautifulSoup (response.content, "html5lib")
    soup = soup.find ("a", class_="active")
    maxEpisodes = int (soup.get("ep_end"))
    try:
        episode = int (input ("{}Select Episode {}[{}]:".format(BLUE,WHITE,f"1-{soup.get('ep_end')}")))
    except:
        killProgram()
    if episode <= 0 or episode > maxEpisodes: killProgram()
    return episode, maxEpisodes

def getQualities (link):
    res = requests.get(link)
    soup = BeautifulSoup(res.content, "html5lib")
    soup = soup.findAll ("div", class_="dowload")
    q = []
    for i in soup:
        i = str (i)
        if "360P - mp4" in i: q.append(360)
        if "480P - mp4" in i: q.append(480)
        if "720P - mp4" in i: q.append(720)
        if "1080P - mp4" in i: q.append(1080)
    return q

def selectQuality (link):
    quals = getQualities (link)
    dp = {}
    c = 1
    txt = GREEN + "Available Qualities " + WHITE + "="
    for i in quals:
        dp[c] = i
        txt = txt + " " + MAGENTA + str (c) + WHITE + ". " + str(i) + " " + WHITE
        c += 1
    print (txt)
    try :
        q = int (input ("Select Quality = "))
    except:
        killProgram()
    if q <= 0 or q > len (dp): killProgram()
    return dp[q]

def getEmbeddedLink(Name, Ep):
    url = f'{provider}/{Name}-episode-{Ep}' # impt link
    res = requests.get(url)
    soup = BeautifulSoup(res.content, "html5lib")
    soup = soup.findChild("li", class_="dowloads")
    soup = str (soup)
    link_to_get_quality = soup[soup.index("https://") : soup.index('" target=')]
    qual = selectQuality(link_to_get_quality) # we have the quality, the user wants
    #
    res = requests.get(url)
    soup = BeautifulSoup(res.content, "html5lib")
    soup = soup.find("li", class_="vidcdn")
    soup = str(soup)
    soup = soup[soup.index('data-video="//'):soup.index('" ')]
    soup = "https:" + soup[12:]
    soup = soup.replace("amp;","&")
    link = soup
    embedded = link
    res = requests.get(link)
    soup = BeautifulSoup(res.content, "html5lib")
    soup = str (soup)
    idx = soup.index ("m3u8")
    stuff = soup[idx-150:idx]
    stuff = stuff[stuff.index('https://'):]
    stuff = stuff + str(qual) + ".m3u8"
    main = stuff
    return embedded, main
def storeInHistory(anime):
    os.system(f"echo {anime} >> history.txt")
def chooseFromHistory (names):
    dp = {}
    c = 1
    for i in names :
        dp[c] = i
        c+=1
    for i, j in dp.items():
        print (i,j)
    try :
        ch = int (input ("Enter choice : "))
    except:
        killProgram()
    if ch <= 0 or ch >= c: killProgram()

    # print ('chosen history = ', dp[ch])
    choice = dp[ch]

    episode, maxepisodes = getEpisode(choice)

    
    while episode <= maxepisodes :
        embedded, main = getEmbeddedLink (choice, episode)
        cmd = 'mpv.com --http-header-fields="Referer: {}" "{}"'.format(embedded, main)
        print ("Your Anime is starting.....")
        print (f"Currently Playing : {choice} episode {episode}")
        os.system(cmd)
        print ("To watch the next episode, press n")
        print ("To exit, press e")
        opt = input ()
        if opt == "n": episode += 1; continue
        else : break
    print ("You have completed watching {} episode {}".format(choice,max(episode,maxepisodes)))
    print ("If you like the app, please star it on github !")
    print ("Visit - https://github.com/purplevarun/watchanime")
    input("Press any key to exit")
    exit (0)

def showHistory():
    file = open ("history.txt", "r")
    file = file.read()
    file = file.split ("\n")
    file = file[:-1]
    file = [i.strip() for i in file]
    ch = input ("You were already watching anime, do you want to resume ? (y/n)")
    if ch == 'y':
        chooseFromHistory(file)
    else : return
def main():
    if os.path.exists("history.txt"):
        showHistory()

    Name = input (GREEN+"Enter Name of Anime : "+WHITE)
    #
    Possibilities = getNames(Name)
    #
    choice = getChoice (Possibilities)
    #
    episode, maxepisodes = getEpisode(choice)
    storeInHistory(f"{choice}")
    #
    while episode <= maxepisodes :
        embedded, main = getEmbeddedLink (choice, episode)
        cmd = 'mpv.com --http-header-fields="Referer: {}" "{}"'.format(embedded, main)
        print ("Your Anime is starting.....")
        print (f"Currently Playing : {choice} episode {episode}")
        os.system(cmd)
        print ("To watch the next episode, press n")
        print ("To exit, press e")
        opt = input ()
        if opt == "n": episode += 1; continue
        else : break
    print ("You have completed watching {} episode {}".format(choice,min(episode,maxepisodes)))
    print ("If you like the app, please star it on github !")
    print ("Visit - https://github.com/purplevarun/watchanime")
    input("Press any key to exit")
if __name__ == '__main__': 
    main()
