import os
import sys
import time
from frames import save_frames, get_tracks
from spotifyclient import SpotifyClient
from video import apply_edits


def main():
    vid = "download.mp4"
    apply_edits(vid)

    while not os.path.exists('final.mp4'):
        time.sleep(1)
    save_frames()

    while not os.path.exists('image_frames'):
        time.sleep(1)

    # while not os.path.isdir(
    #         "C:/Users/leora/PycharmProjects/spotifyReader/image_frames"):
    #     time.sleep(1)

    # time.sleep(20)
    plst = {}
    trackdict = get_tracks(plst)

    time.sleep(5)
    spotify_client = SpotifyClient(os.getenv("SPOTIFY_AUTHORIZATION_TOKEN"),
                                   os.getenv("SPOTIFY_USER_ID"))
    try:
        tracks = [spotify_client.get_track_id(song, artist) for song, artist in
                trackdict.items()]
    except KeyError:
        sys.exit("Authorization token has probably expired.")

    name = input("What would you like the name of your playlist to be?")
    public = input("Would you like this playlist to be public? (y/n)")
    while True:
        if public == "y" or "n":
            if public == "y":
                public = True

            elif public == "n":
                public = False
            break
        else:
            print("Invalid. Try again.")

    playlist = spotify_client.create_playlist(name, public)
    time.sleep(10)
    spotify_client.add_to_playlist(playlist, tracks)


if __name__ == "__main__":
    main()

# https://accounts.spotify.com/authorize?client_id=1bda063aaccb468087057d9a1c845e48&response_type=code&redirect_uri=https%3A%2F%2Fgithub.com%2F20leo02%2FTikstract
