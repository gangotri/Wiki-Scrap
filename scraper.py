import requests
from bs4 import BeautifulSoup

import json


def parseUrl (wiki_url):
    response = requests.get(
        url = wiki_url
    )
    soup = BeautifulSoup(response.content, "html.parser")
    return soup

def getTitle (soup):
    title = soup.find(id = "firstHeading")
    return title.string

def getDescription(soup):
    toc = soup.find(id = "toc")
    ul = toc.find("ul")
    return createJson(ul, soup)

def createJson(ul, soup):
    result = {}
    for li in ul.find_all("li", recursive=False):
        
        key = li.find("span", { "class" : "toctext" }).string
        ul = li.find("ul")
        if ul:
            result[key] = [createJson(ul, soup)]
        else:
            result[key] = getParaText(li, soup)
    return result

def getParaText(li, soup):
    linkId = li.find("a")["href"]
    paraId = linkId.replace("#","")
    para = soup.find(id = paraId).parent.find_next("p")
    desc = None
    if(para != None):
        desc = soup.find(id = paraId).parent.find_next("p").get_text()
    return desc


