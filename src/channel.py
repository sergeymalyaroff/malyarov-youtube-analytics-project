import json
import requests
import os


class Channel:
    BASE_URL = "https://www.googleapis.com/youtube/v3/channels"

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
        self.subscriber_count = data['statistics']['subscriberCount']
        self.video_count = data['statistics']['videoCount']
        self.view_count = data['statistics']['viewCount']

    def get_channel_data(self):
        params = {
            'part': 'snippet,statistics',
            'id': self.channel_id,
            'key': self.api_key
        }
        response = requests.get(self.BASE_URL, params=params)
        data = response.json()
        return data.get('items')[0] if data.get('items') else None

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
