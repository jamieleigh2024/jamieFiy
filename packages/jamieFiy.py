import requests
import os

from artists import Artists
from albums import Albums
from playlists import Playlists


class JamieFiy():

    def __init__(self):
        self.client_id = "86d2d7b67f5047f4872829fdad863850"
        self.client_secret = os.environ['SEAN_SPOTIFY_API_KEY']
        self.app_name = "testapp-1"
        self.token_url = "https://accounts.spotify.com/api/token"
        self.api_url = "https://api.spotify.com/v1"
        self.token_headers = {
            "Content-Type": "application/x-www-form-urlencoded"
        }
        self.token_data = {
            "grant_type": "client_credentials",
            "client_id": self.client_id,
            "client_secret": self.client_secret
        }
        self.token = self.get_token()
        self.artists = Artists(self)
        self.albums = Albums(self)
        self.playlists = Playlists(self)
    
    
    def get_token(self):
        """get an access token for spotify api

        :return:
        """
        request = requests.post(url=self.token_url,
                                headers=self.token_headers,
                                data=self.token_data)
        return request.json()['access_token']


jf = JamieFiy()

alexisonfire_artist_id = "53RsXctnNmj9oKXvcbvzI2"
ffaf_artist_id = '4AbDWrmJPSOeIbT2Ou60ik'
alexisonfire = jf.artists.get(alexisonfire_artist_id)
print(alexisonfire)

# alexisonfire_albums = jf.artists.get_albums(alexisonfire_artist_id)
# print(alexisonfire_albums['items'][0])

# alexisonfire_top_tracks = jf.artists.get_top_tracks(alexisonfire_artist_id)
# print(alexisonfire_top_tracks['tracks'][1]['name'])

# alexisonfire_related_artists = jf.artists.get_related_artists(alexisonfire_artist_id)
# print(alexisonfire_related_artists)

# new_releases = jf.albums.get_new_releases(limit=49)
# print(new_releases['albums']['items'])

# my_saved_albums = jf.albums.get_users_saved_albums(limit=20, offset=0)
# print(my_saved_albums)
# throws a 403 error forbidden

# album_tracks = jf.albums.get_tracks(album_id='1LOJfNDxQhbpssKx7oM7at?si=pmixRLKjTdaO1XuPBHZKJQ')
# print(album_tracks)

# playlist = jf.playlists.get(playlist_id='62wW67yRcDrZunRQlgzsqU?si=f13566d07d8140ce')
# print(playlist)

# playlist_tracks = jf.playlists.get_tracks(playlist_id='62wW67yRcDrZunRQlgzsqU?si=f13566d07d8140ce')
# print(playlist_tracks)

# current_users_playlist = jf.playlists.get_current_users_playlists(limit=20, offset=0)
# print(current_users_playlist)
# throws a 401 error missing token? 

# a_users_playlists = jf.playlists.get_a_users_playlitst(user_id='1133074962' , limit=20, offset=0)
# print(a_users_playlists)

# featured_playlists = jf.playlists.get_featured_playlists(limit=20, offset=0)
# print(featured_playlists)

# category_playlist = jf.playlists.get_category_playlists(catagory='pop')
# print(category_playlist)

# cover_image = jf.playlists.get_cover_image(playlist_id='4VG4dvfYLkb07UtLhseEij?si=d43bfc9af7374c2e')
# print(cover_image)
#return doesnt look like the respons sample