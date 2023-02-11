import requests

url = "https://gowatch.p.rapidapi.com/lookup/title/tmdb_id"

querystring = {"id":"496243","type":"movie","country":"us"}

payload = "id=496243&type=movie&country=us"
headers = {
	"content-type": "application/x-www-form-urlencoded",
	"X-RapidAPI-Key": "20719788e5msh46d7f8c7ed9abd9p1d8da2jsnb3f8e9ee7b85",
	"X-RapidAPI-Host": "gowatch.p.rapidapi.com"
}

response = requests.request("POST", url, data=payload, headers=headers, params=querystring)

print(response.text)

