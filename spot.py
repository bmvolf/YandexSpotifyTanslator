import spotipy
import FileManager
import json
import Data
from spotipy.oauth2 import SpotifyOAuth

scope = "playlist-modify-public playlist-modify-private user-library-read"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id = Data.client_id,
    client_secret = Data.client_secret,
    redirect_uri = "http://127.0.0.1:8000/callback",
    scope = scope
))

#Take ID
user_id = sp.current_user()['id']
allData = json.loads(FileManager.read())
names = allData[0]
arts = allData[1]
#Search of tracks
track_uris = []
for i in range(len(names)):
    res = sp.search(q = f'artist:{arts[i]} track:{names[i]}', type='track', limit = 1)
    items = res['tracks']['items']
    if items:
        track_uris.append(res['tracks']['items'][0]['uri'])
    else:
        continue

#Creating platlist
playlist = sp.user_playlist_create(
    user = user_id,
    name = allData[2],
    public = True,
    description = "Создано через Перевод"
)

#Tracks add
sp.playlist_add_items(playlist_id=playlist['id'], items=track_uris)

print("✅ Плейлист создан:", playlist['external_urls']['spotify'])