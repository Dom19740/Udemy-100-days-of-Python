import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from bs4 import BeautifulSoup

SPOTIPY_CLIENT_ID = '632fa3b8b7ff434081aa04fc471daa5f'
SPOTIPY_CLIENT_SECRET = '7e0cdcf62a5144baa047435ac49fd450'

# Get list of songs from a year
# date = input("What year do you want to travel to? Format YYYY-MM-DD: ")
date = "1990-06-10"

response = requests.get(f"https://www.billboard.com/charts/hot-100/{date}/")
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")
song_names_text = soup.find_all("h3", class_="a-no-trucate")
song_names = [song.getText().strip() for song in song_names_text]

# set up spotify
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=SPOTIPY_CLIENT_ID,
        client_secret=SPOTIPY_CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]

song_uris = []
year = date.split("-")[0]
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")


playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
print(playlist)

sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
