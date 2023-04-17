import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

SPOTIPY_CLIENT_ID = "1408478479df4bd98acd08e126dbbeab"
SPOTIPY_CLIENT_SECRET = "e7bb2cf239304e17957a65cc1af46e94"
REDIRECT_URL = "http://example.com"
SCOPE = "playlist-modify-private"
USERNAME = "wentung"

# year_to_travel = input("Which year do you want to travel to? YYYY-MM-DD")
# https://spotipy.readthedocs.io/en/2.13.0/?highlight=user_playlist_create#spotipy.client.Spotify.user_playlist_create

# scratching the billboard
res = requests.get("https://www.billboard.com/charts/hot-100/2010-08-12/")
content = res.text
soup = BeautifulSoup(content, "html.parser")
song_titles = [title.get_text(strip=True)
               for idx, title in enumerate(soup.select(".lrv-u-width-100p #title-of-a-story.c-title.a-no-trucate"))]

# get the spotify auth https://www.youtube.com/watch?v=lykCVzomVvQ
auth_manager = spotipy.oauth2.SpotifyOAuth(
    client_id=SPOTIPY_CLIENT_ID,
    client_secret=SPOTIPY_CLIENT_SECRET,
    redirect_uri=REDIRECT_URL,
    scope=SCOPE,
    username=USERNAME
)
sp = spotipy.Spotify(auth_manager=auth_manager)


### get spotipy playlist
# auth_manager = SpotifyClientCredentials(client_id=SPOTIPY_CLIENT_ID, client_secret=SPOTIPY_CLIENT_SECRET)
# sp = spotipy.Spotify(auth_manager=auth_manager)
#
# playlists = sp.user_playlists('spotify')
# while playlists:
#     for i, playlist in enumerate(playlists['items']):
#         print("%4d %s %s" % (i + 1 + playlists['offset'], playlist['uri'], playlist['name']))
#     if playlists['next']:
#         playlists = sp.next(playlists)
#     else:
#         playlists = None
