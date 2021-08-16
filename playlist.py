class Playlist:
    """Represents a Spotify playlist."""

    def __init__(self, name, id):
        """
        :param name: Name of playlist
        :type name: String
        :param id: Playlist ID
        :type id: int
        """
        self.name = name
        self.id = id

    def __str__(self):
        return f'Playlist: {self.name}'

