from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from pprint import pprint

SPOTIFY_CLIENT_ID = "############"
SPOTIFY_CLIENT_SECRET = "####################"

auth_manager = SpotifyOAuth(
    client_id=SPOTIFY_CLIENT_ID,
    client_secret= SPOTIFY_CLIENT_SECRET,
    redirect_uri= "http://example.com/callback/",
    scope=  "playlist-read-collaborative playlist-modify-public playlist-read-private playlist-modify-private",
    cache_path= "token.txt"
    
)

sp = spotipy.Spotify(auth_manager= auth_manager)
user_id = sp.current_user()['id']


date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD\n")
year = date.split("-")[0]
url = f"https://www.billboard.com/charts/hot-100/{date}"

response = requests.get(url)
website = response.text

soup = BeautifulSoup(website, "html.parser")

all_title_tags = soup.select("li ul li h3", id="title-of-a-story")

song_names = []
for tag in all_title_tags:
   song_names.append(tag.getText().strip())


songs_uris = []
for song in song_names:
    song_data = sp.search(f"track:{song} year:{year}", 1)
    songs_uris.append(song_data['tracks']['items'][0]['uri'])
playlist = sp.user_playlist_create(user_id, name=f"{date} Billboard 100")
sp.playlist_add_items(playlist['id'], items=songs_uris)



