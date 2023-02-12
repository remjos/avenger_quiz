import requests
import json

url = "https://imdb8.p.rapidapi.com/auto-complete"

querystring = {"q":"game"}

headers = {
	"X-RapidAPI-Key": "dea9a5d159msha8ea04001912514p1cc719jsn81e0afc8ee63",
	"X-RapidAPI-Host": "imdb8.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

# json = response.json()

# image = json.get("l").get("imageUrl")

print(response.text)

