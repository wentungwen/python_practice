from models import UserModel
from spotify_manager import SpotifyManager
from spotipy import Spotify
from spotipy.oauth2 import SpotifyOAuth
from datetime import datetime, timedelta
import os


SPOTIPY_CLIENT_ID = os.environ.get("SPOTIPY_CLIENT_ID")
SPOTIPY_CLIENT_SECRET = os.environ.get("SPOTIPY_CLIENT_SECRET")
print(SPOTIPY_CLIENT_ID)

REDIRECT_URL = "http://example.com"
SCOPE = "user-library-read playlist-modify-public"
USERNAME = "wentung"

from_date = input("Which year do you want to start? YYYY-MM-DD  ")
to_date = input("Which year do you want to end with? YYYY-MM-DD  ")
start_date = datetime.strptime(from_date, "%Y-%m-%d")
end_date = datetime.strptime(to_date, "%Y-%m-%d")


def create_dates_list(start_d, end_d):
    dates = []
    current_date = start_d
    while current_date <= end_d:
        dates.append(current_date.strftime("%Y-%m-%d"))
        current_date += timedelta(days=180)
    return dates


spotify_manager = SpotifyManager()
now_date = datetime.today().date()

for input_date in create_dates_list(start_date, end_date):
    try:
        input_date = datetime.fromisoformat(input_date).date()
    except ValueError as e:
        print("Incorrect data format, should be YYYY-MM-DD")
        raise SystemExit
    else:
        if input_date >= now_date:
            print("Out of date range! Try other dates.")
            raise SystemExit

    # New authentication
    auth_manager = SpotifyOAuth(
        client_id=SPOTIPY_CLIENT_ID,
        client_secret=SPOTIPY_CLIENT_SECRET,
        redirect_uri=REDIRECT_URL,
        scope=SCOPE,
        username=USERNAME)
    sp_auth = Spotify(auth_manager=auth_manager)

    # get the user info and write it into UserData
    u_data = sp_auth.current_user()
    user_model = UserModel(
        user_name=u_data["display_name"],
        user_external_url=u_data["external_urls"]["spotify"],
        user_href=u_data["href"],
        user_id=u_data["id"],
        user_uri=u_data["uri"]
    )

    # search for the playlist. If playlist has already existed then return url, if not, create the playlist
    playlist_data = sp_auth.user_playlists(user_model.user_id)
    is_playlist_exist = True

    for playlist in playlist_data["items"]:
        if f"{input_date} Billboard 100" in playlist.values():
            print(f'The playlist is here: {playlist_data["items"][0]["external_urls"]["spotify"]}')
        else:
            is_playlist_exist = False

    if not is_playlist_exist:
        # search for songs' title of that date
        song_list = spotify_manager.scratching_billboard(input_date)
        while not song_list:
            print("try another date or check again the format.")
            song_list = spotify_manager.scratching_billboard(input_date)

        # create playlist
        playlist = sp_auth.user_playlist_create(
            user=user_model.user_id,
            name=f"{input_date} Billboard 100",
            public=True,
            description=f"{input_date} Billboard 100"
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
