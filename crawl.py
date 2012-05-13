import requests
from bs4 import BeautifulSoup
import redis
from documentModel import *

#parse front page of hacker news
url = 'http://news.ycombinator.com/'
r = requests.get(url)
soup = BeautifulSoup(r.text)
docModel = DocumentModel()
#docModel.CreateTable()

#snag the links
for link in soup.find_all('a'):
	loc = link.get('href')
	#for now we don't want anything that is in the ycombinator domain
	if loc.count('http') != 0:
		#lets persist links with redis
		docModel.InsertLocation(loc)