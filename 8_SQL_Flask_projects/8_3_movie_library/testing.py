import requests

url = "https://api.themoviedb.org/3/search/movie?"

headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJhYzYzZWY5YjFjMTkwMzI2N2M3NGZiMmIxNjcyMTUyZSIsInN1YiI6IjYwMDk4ODNlZGQ4M2ZhMDA0MDhkMDY5YSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.yigJaO5PRADK1QmdJw21v0afPrXswv-hb3qKQoQlcA8"
}
params = {
    "query": "it",
    "page": 1,
    "language": "en-US"
}

response = requests.get(url, headers=headers, params=params)
movie_data = response.json()["results"][0]

title = movie_data["title"]
description = movie_data["overview"]
img_url= movie_data["poster_path"]
year = movie_data["release_date"]

print(f"https://api.themoviedb.org/3/search/movie/{img_url}")


