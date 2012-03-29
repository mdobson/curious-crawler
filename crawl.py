import requests
from bs4 import BeautifulSoup
import redis

#parse front page of hacker news
url = 'http://news.ycombinator.com/'
r = requests.get(url)
soup = BeautifulSoup(r.text)


#lets make a connection to redis

redis_server = redis.Redis("localhost")
#snag the links
for link in soup.find_all('a'):
	loc = link.get('href')
	#for now we don't want anything that is in the ycombinator domain
	if loc.count('http') != 0:
		#lets persist links with redis
		print redis_server.rpush("index",loc)