import requests


class Albums:

    def __init__(self, jamiefy):    
        self.jamiefy = jamiefy
        self.endpoint_url = "albums"

    
    def get(self, album_id):
        album = requests.get(
            url=f"{self.jamiefy.api_url}/{self.endpoint_url}/{album_id}",
            headers={
                "Authorization": f"Bearer {self.jamiefy.token}"
            }
        )
        return album.json()

    
    def get_tracks(self, album_id):
        album_tracks = requests.get(
            url=f"{self.jamiefy.api_url}/{self.endpoint_url}/{album_id}/tracks",
            headers={
                "Authorization": f"Bearer {self.jamiefy.token}"
            }
        )
        return album_tracks.json()

    
    def get_users_saved_albums(self, limit=20, offset=0):
        saved_albums = requests.get(
            url=f"{self.jamiefy.api_url}/me/albums?offset={offset}&limit={limit}",
            headers={
                "Authorization": f"Bearer {self.jamiefy.token}"
            }
        )
        return saved_albums.json()    

    
    def get_new_releases(self, limit=20, offset=0):
        assert limit in range(0, 51)
        new_releases = requests.get(
            url=f"{self.jamiefy.api_url}/browse/new-releases?limit={limit}",
            headers={
                "Authorization": f"Bearer {self.jamiefy.token}"
            }
        )
        return new_releases.json()


