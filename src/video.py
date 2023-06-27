
import json

class Video:
    def __init__(self, id, title, url, views, likes):
        self.id = id
        self.title = title
        self.url = url
        self.views = views
        self.likes = likes

    def __repr__(self):
        return f"Video('{self.id}', '{self.title}', '{self.url}', {self.views}, {self.likes})"

class PLVideo(Video):
    def __init__(self, id, title, url, views, likes, playlist_id):
        super().__init__(id, title, url, views, likes)
        self.playlist_id = playlist_id

    def __repr__(self):
        return f"PLVideo('{self.id}', '{self.title}', '{self.url}', {self.views}, {self.likes}, '{self.playlist_id}')"
