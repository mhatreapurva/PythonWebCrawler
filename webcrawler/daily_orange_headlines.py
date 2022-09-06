from ast import List

import requests
from bs4 import BeautifulSoup


def returnTitles(url: str) -> List:
    try:
        titles = [] 
        f = requests.get(url)
        soup = BeautifulSoup(f.content, 'lxml')
        head_tags = soup.find_all(['h4'])
        titles = [str(title.contents[0]).rstrip().lstrip() for title in head_tags]
        titles = list(filter(len, titles))
    except:
        print("Titles could not be found")
    return titles if titles else []

def printTitles(data: List):
    for idx,title in enumerate(data[:-6]):
        print(f"{idx+1}: {title}")
