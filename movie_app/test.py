import requests
import json
import pprint
from bs4 import BeautifulSoup


url = "https://utelly-tv-shows-and-movies-availability-v1.p.rapidapi.com/lookup"

# todo - put an input here to get a specific query for the user

querystring = {"term": "startrek", "country": "us"}

headers = {
    #where api goes
}

response = requests.request(
    "GET", url, headers=headers, params=querystring).json()



# data = response.json()


#name = data['name']
# picture = data['picture']

# print(f"{name} has the picture of {picture}")
#print(name)

# where_to_watch = data['locations']
# print(where_to_watch)
# print(response.json())
pprint.pprint(response)


