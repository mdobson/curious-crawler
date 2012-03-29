import redis
import requests
from bs4 import BeautifulSoup

#create redis connection
redis_server = redis.Redis("localhost")

#read a link from the redis index
requrl = redis_server.lindex("index",2)

#parse up the content
r = requests.get(requrl)
soup = BeautifulSoup(r.text)

#holds all the page qualifying data
qualifier = {}

#for all the content in the page
for content in soup.find_all('p'):
	words = content.get_text().split()
	#add to dictionary. If it doesnt exist add it with an instance of 1 else increment it
	for word in words:
		if not word in qualifier:
			qualifier[word] = 1
		else:
			qualifier[word] += 1

#sort it from greatest to least, add it to a redis hashset
for pair in sorted(qualifier.items(), key=lambda(k,v):(v,k),reverse=True):
	redis_server.hset(requrl,pair[0],pair[1])