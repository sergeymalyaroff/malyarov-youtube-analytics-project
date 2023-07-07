import json
import requests
import os


class Channel:
    BASE_URL = "https://www.googleapis.com/youtube/v3/channels"
    YT_API_KEY = "AIzaSyA38Js6ZuOi3612bTl_vTmcqxO_7i0BQEw"

    def __init__(self, channel_id: str) -> None:
        self.channel_id = channel_id
        self.api_key = os.environ.get('YT_API_KEY')
        if self.api_key is None:
            raise Exception("YT_API_KEY is not set in the environment variables.")

        data = self.get_channel_data()
        if not data:
            raise Exception(f"Channel with id {self.channel_id} does not exist.")

        self.title = data['snippet']['title']
        self.description = data['snippet']['description']
        self.url = f"https://www.youtube.com/channel/{self.channel_id}"
        self.subscriber_count = int(data['statistics']['subscriberCount'])
        self.video_count = int(data['statistics']['videoCount'])
        self.view_count = int(data['statistics']['viewCount'])

    def get_channel_data(self):
        params = {
            'part': 'snippet,statistics',
            'id': self.channel_id,
            'key': self.api_key
        }
        response = requests.get(self.BASE_URL, params=params)
        data = response.json()
        return data.get('items')[0] if data.get('items') else None

    def __str__(self):
        return f'{self.title} ({self.url})'

    def __add__(self, other):
        if isinstance(other, Channel):
            return self.subscriber_count + other.subscriber_count
        else:
            raise TypeError("Can only add two Channel instances")

    def __sub__(self, other):
        if isinstance(other, Channel):
            return self.subscriber_count - other.subscriber_count
        else:
            raise TypeError("Can only subtract two Channel instances")

    def __eq__(self, other):
        if isinstance(other, Channel):
            return self.subscriber_count == other.subscriber_count
        else:
            return False

    def __ne__(self, other):
        if isinstance(other, Channel):
            return self.subscriber_count != other.subscriber_count
        else:
            return True

    def __lt__(self, other):
        if isinstance(other, Channel):
            return self.subscriber_count < other.subscriber_count
        else:
            return False

    def __le__(self, other):
        if isinstance(other, Channel):
            return self.subscriber_count <= other.subscriber_count
        else:
            return False

    def __gt__(self, other):
        if isinstance(other, Channel):
            return self.subscriber_count > other.subscriber_count
        else:
            return False

    def __ge__(self, other):
        if isinstance(other, Channel):
            return self.subscriber_count >= other.subscriber_count
        else:
            return False

    @classmethod
    def get_service(cls):
        from googleapiclient.discovery import build
        api_key = os.environ.get('YT_API_KEY')
        return build('youtube', 'v3', developerKey=api_key)

    def to_json(self, filename: str):
        data = {
            'channel_id': self.channel_id,
            'title': self.title,
            'description': self.description,
            'url': self.url,
            'subscriber_count': self.subscriber_count,
            'video_count': self.video_count,
            'view_count': self.view_count
        }
        with open(filename, 'w') as f:
            json.dump(data, f)

    def print_info(self) -> None:
        print(f"Title: {self.title}")
        print(f"Description: {self.description}")
        print(f"URL: {self.url}")
        print(f"Subscriber count: {self.subscriber_count}")
        print(f"Video count: {self.video_count}")
        print(f"View count: {self.view_count}")
