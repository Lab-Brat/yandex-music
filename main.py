import sys, os
from yandex_music import Client


class Music():
    def __init__(self):
        self.token = self.get_token('token')
        self.client = self.authenticate()

    def get_token(self, token_file):
        with open(token_file, 'r') as f:
            return f.readlines()[0]

    def authenticate(self):
        sys.stdout = open(os.devnull, 'w')
        client = Client(self.token).init()
        sys.stdout = sys.__stdout__
        return client

    def get_liked_songs(self):
        likes = self.client.users_likes_tracks()[0].fetch_track()
        print(likes.title)
        print(likes.artists[0]['name'])


if __name__ == '__main__':
    ym = Music()
    ym.get_liked_songs()
