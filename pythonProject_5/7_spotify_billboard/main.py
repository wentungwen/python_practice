import requests

# year_to_travel = input("Which year do you want to travel to? YYYY-MM-DD")
# https://spotipy.readthedocs.io/en/2.13.0/?highlight=user_playlist_create#spotipy.client.Spotify.user_playlist_create

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

auth_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(auth_manager=auth_manager)

playlists = sp.user_playlists('spotify')
while playlists:
    for i, playlist in enumerate(playlists['items']):
        print("%4d %s %s" % (i + 1 + playlists['offset'], playlist['uri'],  playlist['name']))
    if playlists['next']:
        playlists = sp.next(playlists)
    else:
        playlists = None
