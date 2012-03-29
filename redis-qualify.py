import redis


redis_server = redis.Redis("localhost")

stopwords = ["it","is","and","a","this","the","too","to","also"]

#read a link from the redis index
requrl = redis_server.lindex("index",2)

qualifier = redis_server.hgetall(requrl)

for pair in qualifier:
	if len(pair) > 8:
		print pair

