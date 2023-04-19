from user_data import UserData
from spotify_manager import SpotifyManager

from spotipy import Spotify
from spotipy.oauth2 import SpotifyOAuth


SPOTIPY_CLIENT_ID = "1408478479df4bd98acd08e126dbbeab"
SPOTIPY_CLIENT_SECRET = "e7bb2cf239304e17957a65cc1af46e94"
REDIRECT_URL = "http://example.com"
SCOPE = "user-library-read playlist-modify-public"
USERNAME = "wentung"

date = input("Which year do you want to travel to? YYYY-MM-DD  ")
spotify_manager = SpotifyManager()

if spotify_manager.check_date(date):
    # get the user info and write it into UserData
    auth_manager = SpotifyOAuth(
        client_id=SPOTIPY_CLIENT_ID,
        client_secret=SPOTIPY_CLIENT_SECRET,
        redirect_uri=REDIRECT_URL,
        scope=SCOPE,
        username=USERNAME)
    sp_auth = Spotify(auth_manager=auth_manager)
    data = sp_auth.current_user()
    user_data = UserData(
        user_name=data["display_name"],
        user_external_url=data["external_urls"]["spotify"],
        user_href=data["href"],
        user_id=data["id"],
        user_uri=data["uri"]
    )

    # search for the playlist. If playlist has already existed then return url, if not, create the playlist
    playlist_data = sp_auth.user_playlists(user_data.user_id)
    is_playlist_exist = True

    for playlist in playlist_data["items"]:
        if f"{date} Billboard 100" in playlist.values():
            print(f'The playlist is here: {playlist_data["items"][0]["external_urls"]["spotify"]}')
        else:
            is_playlist_exist = False

    if not is_playlist_exist:
        # search for songs' title of that date

        song_list = spotify_manager.scratching_billboard(date)
        while not song_list:
            print("try another date or check again the format.")
            song_list = spotify_manager.scratching_billboard(date)

        # create playlist
        playlist = sp_auth.user_playlist_create(
            user=user_data.user_id,
            name=f"{date} Billboard 100",
            public=True,
            description=f"{date} Billboard 100"
        )
        playlist_id = playlist["id"]

        # search for a song
        for idx, song in enumerate(song_list):
            result = sp_auth.search(q=song_list[idx], type='track', limit=1)
            if len(result["tracks"]["items"]) > 0:
                first_result = result["tracks"]["items"][0]
                uri = first_result["uri"]
                external_url = first_result["external_urls"]["spotify"]

                # add the song to the playlist
                sp_auth.playlist_add_items(
                    playlist_id=playlist_id,
                    items=[uri],
                )
                print(f"URL: {external_url}")
