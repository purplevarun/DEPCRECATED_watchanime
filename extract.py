import requests
from bs4 import BeautifulSoup
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
        # print (x)
        title = x.get('href')
        title = list (title)
        title = title[10:]
        title = ''.join(title)
        Animes.append(title)
    return Animes

def getIndexDict (animes):
    count = 1
    dp = {}
    for i in animes:
        dp[count] = i
        count += 1
    return dp