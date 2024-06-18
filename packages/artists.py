import requests


class Artists:

    def __init__(self, jamiefy):
        self.jamiefy = jamiefy
        self.endpoint_url = "artists"

    def get(self, artist_id):
        artist = requests.get(
            url=f"{self.jamiefy.api_url}/{self.endpoint_url}/{artist_id}",
            headers={
                "Authorization": f"Bearer {self.jamiefy.token}"
            }
        )
        return artist.json()

    def get_albums(self, artist_id):
        albums = requests.get(
            url=f"{self.jamiefy.api_url}/{self.endpoint_url}/{artist_id}/albums",
            headers={
                "Authorization": f"Bearer {self.jamiefy.token}"
            }
        )
        return albums.json()

    def get_top_tracks(self, artist_id):
        top_tracks = requests.get(
            url=f"{self.jamiefy.api_url}/{self.endpoint_url}/{artist_id}/top-tracks",
            headers={
                "Authorization": f"Bearer {self.jamiefy.token}"
            }
        )
        return top_tracks.json()

    def get_related_artists(self, artist_id):
        related_artists = requests.get(
            url=f"{self.jamiefy.api_url}/{self.endpoint_url}/{artist_id}/related-artists",
            headers={
                "Authorization": f"Bearer {self.jamiefy.token}"
            }
        )
        return related_artists.json()