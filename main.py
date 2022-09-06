from typing import List
import requests
import xml
from bs4 import BeautifulSoup
from webcrawler.daily_orange_headlines import returnTitles,printTitles

URL = "https://dailyorange.com/"

titlesDailyOrange = returnTitles(url = URL)
printTitles(titlesDailyOrange)






