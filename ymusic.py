import sys, os
from yandex_music import Client


class Music():
    def __init__(self):
        self.token = self.get_token('token')
        self.client = self.authenticate()

    def get_token(self, token_file):
        '''
        Read API token from a text file,
        Return token in string format.
        '''
        with open(token_file, 'r') as f:
            return f.readlines()[0]

    def authenticate(self):
        '''
        Use token for authentication,
        All output in this method is supressed.
        Return authenticated client object
        '''
        sys.stdout = open(os.devnull, 'w')
        client = Client(self.token).init()
        sys.stdout = sys.__stdout__
        return client

    def get_liked_songs(self, write=False):
        '''
        Get (name, artist) from every liked track,
        Return a list of tuples
        '''
        likes = self.client.users_likes_tracks()
        tracks = []
        for i, track in enumerate(likes):
            info = track.fetch_track()
            tracks.append((info.title, info.artists[0]['name']))
            if (i+1) % 20 == 0:
                print(f'Read {i+1} tracks')

        if write == True:
            self.write(tracks)
        
        return tracks

    def write(self, content):
        '''
        Write information about liked songs to a text file
        '''
        with open('content.txt', 'w') as f:
            [f.write(f"Name:{line[0]}, Artist: {line[1]}\n") for line in content]


if __name__ == '__main__':
    ym = Music()
    likes = ym.get_liked_songs(write=True)
