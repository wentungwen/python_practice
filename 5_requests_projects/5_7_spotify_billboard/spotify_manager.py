from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import requests


class SpotifyManager:
    def __init__(self):
        pass

    def get_spotipy_playlist(self, client_id, client_secret):
        """get spotipy's playlist"""
        auth = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
        sp_object = spotipy.Spotify(auth_manager=auth)
        playlists = sp_object.user_playlists('spotify')
        while playlists:
            for i, playlist in enumerate(playlists['items']):
                print("%4d %s %s" % (i + 1 + playlists['offset'], playlist['uri'], playlist['name']))
            if playlists['next']:
                playlists = sp_object.next(playlists)
            else:
                playlists = None

    def scratching_billboard(self, date=str):
        """scratching the billboard and return titles list"""
        res = requests.get(f"https://www.billboard.com/charts/hot-100/{date}/")
        content = res.text
        soup = BeautifulSoup(content, "html.parser")
        song_titles = [title.get_text(strip=True)
                       for idx, title in
                       enumerate(soup.select(".lrv-u-width-100p #title-of-a-story.c-title.a-no-trucate"))]
        return song_titles



