import requests


class Artists:

    def __init__(self, jamiefy_parent_class):
        self.jamiefy_parent_class = jamiefy_parent_class
        self.endpoint_url = "artists"

    def get(self, artist_id):
        artist = requests.get(
            url=f"{self.jamiefy_parent_class.api_url}/{self.endpoint_url}/{artist_id}",
            headers={
                "Authorization": f"Bearer {self.jamiefy_parent_class.token}"
            }
        )
        return artist.json()
