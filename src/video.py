import json
import requests

class Video:
    def __init__(self, id, title=None, url=None, views=None, like_count=None):
        self.id = id
        self.title = title
        self.url = url
        self.views = views
        self.like_count = like_count

        try:
            response = requests.get(
                f"https://www.googleapis.com/youtube/v3/videos?part=snippet%2C+statistics&id={id}&key=AIzaSyA38Js6ZuOi3612bTl_vTmcqxO_7i0BQEw"
            )
            data = json.loads(response.text)
            self.title = data['items'][0]['snippet']['title']
            self.url = f"https://www.youtube.com/watch?v={id}"
            self.views = data['items'][0]['statistics']['viewCount']
            self.likes = data['items'][0]['statistics']['likeCount']
        except:
            self.title = None
            self.url = None
            self.views = None
            self.likes = None

    def __repr__(self):
        return f"Video('{self.id}', '{self.title}', '{self.url}', {self.views}, {self.likes})"

class PLVideo(Video):
    def __init__(self, id, title=None, url=None, views=None, likes=None, playlist_id=None):
        super().__init__(id, title, url, views, likes)
        self.playlist_id = playlist_id

        try:
            response = requests.get(
                f"https://www.googleapis.com/youtube/v3/videos?part=snippet%2C+statistics&id={id}&key=AIzaSyA38Js6ZuOi3612bTl_vTmcqxO_7i0BQEw"
            )
            data = json.loads(response.text)
            self.title = data['items'][0]['snippet']['title']
            self.url = f"https://www.youtube.com/watch?v={id}"
            self.views = data['items'][0]['statistics']['viewCount']
            self.likes = data['items'][0]['statistics']['likeCount']

        except:
            self.title = None
            self.url = None
            self.views = None
            self.likes = None
            self.playlist_id = None

    def __repr__(self):
        return f"PLVideo('{self.id}', '{self.title}', '{self.url}', {self.views}, {self.likes}, '{self.playlist_id}')"
