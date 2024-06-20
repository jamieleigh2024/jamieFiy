import requests


class Playlists:
  
  def __init__ (self, jamiefy):
    self.jamiefy = jamiefy
    self.endpoint_url = "playlists"

  
  def get(self, playlist_id):
    playlist = requests.get(
      url=f"{self.jamiefy.api_url}/{self.endpoint_url}/{playlist_id}",
      headers={
        "Authorization": f"Bearer {self.jamiefy.token}"
      }
    )
    return playlist.json()


  def get_tracks(self, playlist_id):
    playlist_tracks = requests.get(
      url=f"{self.jamiefy.api_url}/{self.endpoint_url}/{playlist_id}/tracks",
      headers={
        "Authorization": f"Bearer {self.jamiefy.token}"
      }
    )
    return playlist_tracks.json()

  
  def get_current_users_playlists(self, limit=20, offset=0):
    current_users_playlists = requests.get(
      url=f"{self.jamiefy.api_url}/me/shows?offset={offset}&limit={limit}",
      headers={
        "Authorization": f"Bearer {self.jamiefy.token}"
     }
   )
    return current_users_playlists.json()


  def get_a_users_playlitst(self, user_id, limit=20, offset=0):
    a_users_playlists = requests.get(
      url=f"{self.jamiefy.api_url}/users/{user_id}/playlists?offset={offset}&limit={limit}",
      headers={
        "Authorization": f"Bearer {self.jamiefy.token}"
     }
   )
    return a_users_playlists.json()


  def get_featured_playlists(self, limit=20, offset=0):
    featured_playlists = requests.get(
      url=f"{self.jamiefy.api_url}/browse/featured-playlists?limit={limit}",
      headers={
        "Authorization": f"Bearer {self.jamiefy.token}"
     }
   )
    return featured_playlists.json()


  def get_category_playlists(self, catagory, limit=20, offset=0):
    category_playlists = requests.get(
      url=f"{self.jamiefy.api_url}/browse/categories/{catagory}?limit={limit}",
      headers={
        "Authorization": f"Bearer {self.jamiefy.token}"
     }
   )
    return category_playlists.json()


  def get_cover_image(self, playlist_id):
    cover_image = requests.get(
      url=f"{self.jamiefy.api_url}/{self.endpoint_url}/{playlist_id}/images",
      headers={
        "Authorization": f"Bearer {self.jamiefy.token}"
     }
    )
    return cover_image.json()