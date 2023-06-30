from googleapiclient.discovery import build
import os
import isodate
import datetime


# Ваш API ключ
YOUTUBE_API_KEY = "AIzaSyA38Js6ZuOi3612bTl_vTmcqxO_7i0BQEw"
youtube = build('youtube', 'v3', developerKey=YOUTUBE_API_KEY)

def get_playlist_details(playlist_id: str) -> dict:
    request = youtube.playlists().list(
        part="snippet,contentDetails",
        id=playlist_id
    )
    response = request.execute()

    # Извлекаем детали плейлиста из ответа
    playlist_info = response['items'][0]
    playlist_title = playlist_info['snippet']['title']
    videos = get_playlist_videos(playlist_id)

    return {
        'title': playlist_title,
        'videos': videos
    }

def get_video_details(video_id: str) -> dict:
    request = youtube.videos().list(
        part="snippet,contentDetails,statistics",
        id=video_id
    )
    response = request.execute()

    # Извлекаем детали видео из ответа
    video_info = response['items'][0]
    video_title = video_info['snippet']['title']
    video_url = f"https://www.youtube.com/watch?v={video_id}"
    video_likes = int(video_info['statistics']['likeCount'])
    video_duration = isodate.parse_duration(video_info['contentDetails']['duration']).total_seconds()

    return {
        'title': video_title,
        'url': video_url,
        'likes': video_likes,
        'duration': video_duration
    }

def get_playlist_videos(playlist_id: str) -> list:
    request = youtube.playlistItems().list(
        part="snippet,contentDetails",
        maxResults=50,
        playlistId=playlist_id
    )
    response = request.execute()

    # Извлекаем детали видео из ответа
    videos = []
    for item in response['items']:
        video_id = item['contentDetails']['videoId']
        video = get_video_details(video_id)
        videos.append(video)

    return videos

class PlayList:
    def __init__(self, id: str):
        self.id = id
        self.details = get_playlist_details(id)
        self.title = self.details['title']
        self.url = f"https://www.youtube.com/playlist?list={self.id}"

    @property
    def total_duration(self) -> datetime.timedelta:
        total_seconds = sum(video['duration'] for video in self.details['videos'])
        return datetime.timedelta(seconds=total_seconds)

    def show_best_video(self) -> str:
        best_video = max(self.details['videos'], key=lambda video: video['likes'])
        return best_video['url']
