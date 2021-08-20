import requests
import json
from track import Track
from playlist import Playlist
import time


class SpotifyClient:
    """Performs operations on the Spotify API"""

    def __init__(self, auth_token, user_id):
        """
        :param auth_token: Spotify API token
        :type auth_token: String
        :param user_id: Spotify user ID
        :type user_id: String
        """

        self.auth_token = auth_token
        self.user_id = user_id

    def create_playlist(self, name, public=True):
        """Creates a playlist for the user in Spotify.
        :param name: Name of the playlist
        :type name: String
        :param public: Whether or not the playlist is public
        :return playlist: A Playlist object
        """

        request_body = json.dumps({
            "name": f"{name}",
            "description": "My Tikstract playlist",
            "public": public})

        url = f"https://api.spotify.com/v1/users/{self.user_id}/playlists"

        response = requests.post(
            url,
            data=request_body,
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {self.auth_token}"
            }
        )
        response_json = response.json()
        time.sleep(5)
        playlist_id = response_json["id"]
        playlist = Playlist(name, playlist_id)

        return playlist

    def get_track_id(self, song, artist):
        """Obtain the track ID for a track.
        :param song: The song name
        :type song: String
        :param artist: The artist of the song
        :type artist: String
        :returns track: A fully initialized Track object
        """
        url = f"https://api.spotify.com/v1/search?query={song}+{artist}&&offset=0&limit=20&type=track"
        response = requests.get(
            url,
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {self.auth_token}"
            }
        )
        response_json = response.json()
        songs = response_json["tracks"]["items"]
        if len(songs)>0:
            track_id = songs[0]["id"]
            track = Track(song, track_id, artist)
            return track
        else:
            pass

    def add_to_playlist(self, playlist, tracks):
        """Add the TikTok tracks to a Spotify playlist.

        :param playlist: Playlist name we are adding tracks to
        :type playlist: Playlist
        :param tracks: List of Track objects
        :type tracks: List
        """
        tracks = [track for track in tracks if track is not None]
        tracks_uris = [track.get_track_uri() for track in tracks if track.id is not None]
        data = json.dumps(tracks_uris)
        url = f"https://api.spotify.com/v1/playlists/{playlist.id}/tracks"

        response = requests.post(
            url,
            data=data,
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {self.auth_token}"}
        )
        response_json = response.json()
        return response_json
