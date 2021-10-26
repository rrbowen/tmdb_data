import urllib.request
import os
import json
import time

f = open("api_key", "r")
api_key = f.read()
f.close()

print(api_key)

#if not os.path.exists("json_files"):
#	os.mkdir("json_files")

#response = urllib.request.urlopen("https://api.themoviedb.org/3/movie/latest?api_key=" + api_key )
#json_response = json.load(response)
#movie_end = int(json_response['id'])

#movie_start = movie_end - 10
# movie_start = 0


#for movie_id in range(movie_start, movie_end):
#	print(movie_id)
#	response = urllib.request.urlopen("https://api.themoviedb.org/3/movie/" + str(movie_id) + "?api_key=" + api_key )

#	json_response = json.load(response)

#	f = open("json_files/tmdb" + str(movie_id) + ".json", "w")
#	f.write(json.dumps(json_response))
#	f.close()
#	time.sleep(20)
#



