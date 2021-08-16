class Track:
    """Represents a track on Spotify"""

    def __init__(self,name, id, artist):
        """
        :param name: Song title of the track
        :type name: String
        :param id: Track ID
        :type id: int
        :param artist: Artist of the track
        :type artist: String
        """

        self.name = name
        self.id = id
        self.artist = artist

    def __str__(self):
        return f'{self.name}'

    leo = "so"

