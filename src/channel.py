import requests
import os


class Channel:
    """Класс для ютуб-канала"""

    BASE_URL = "https://www.googleapis.com/youtube/v3/channels"

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel_id = channel_id
        self.api_key = os.environ.get('YT_API_KEY')
        if self.api_key is None:
            raise Exception("YT_API_KEY is not set in the environment variables.")
        self.data = self.get_channel_data()

    def get_channel_data(self):
        params = {
            'part': 'snippet,statistics',
            'id': self.channel_id,
            'key': self.api_key
        }
        response = requests.get(self.BASE_URL, params=params)
        data = response.json()
        return data.get('items')[0] if data.get('items') else None

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        if self.data:
            print(self.data)
        else:
            print(f"Channel with id {self.channel_id} does not exist.")
