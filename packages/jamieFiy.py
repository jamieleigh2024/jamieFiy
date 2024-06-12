import requests
from artists import Artists


class JamieFiy():

    def __init__(self):
        self.client_id = "86d2d7b67f5047f4872829fdad863850"
        self.client_secret = "59e48f28fa254ed09d628e193a76a448"
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

    def get_token(self):
        """get an access token for spotify api

        :return:
        """
        request = requests.post(
            url=self.token_url,
            headers=self.token_headers,
            data=self.token_data
        )
        return request.json()['access_token']



jf = JamieFiy()
print(jf.artists.get('53RsXctnNmj9oKXvcbvzI2'))
