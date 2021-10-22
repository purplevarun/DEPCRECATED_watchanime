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
        title = x.get('title')
        Animes.append(title)
    return Animes