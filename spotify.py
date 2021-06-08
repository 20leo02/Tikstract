import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyOAuth

scope = "user-library-read"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))


artist = 'Moses Sumney'
track = 'Lonely World'

track_id = sp.search(q='artist:' + artist + ' track:' + track, type='track')

print(track_id)
#bruh
print("hey")
def track():
    pass