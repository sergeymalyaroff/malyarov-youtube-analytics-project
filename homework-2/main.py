from src.channel import Channel
from src.video import Video, PLVideo

if __name__ == '__main__':
    moscowpython = Channel('UC-OVMPlMA3-YCIeg4z5z23A')

    # получаем значения атрибутов
    print(moscowpython.title)  # MoscowPython
    print(moscowpython.video_count)  # 685 (может уже больше)
    print(moscowpython.url)  # https://www.youtube.com/channel/UC-OVMPlMA3-YCIeg4z5z23A



    # менять не можем
    moscowpython.channel_id = 'Новое название'
    # AttributeError: property 'channel_id' of 'Channel' object has no setter

    # можем получить объект для работы с API вне класса
    print(Channel.get_service())
    # <googleapiclient.discovery.Resource object at 0x000002B1E54F9750>

    # создаем файл 'moscowpython.json' в данными по каналу
    moscowpython.to_json('moscowpython.json')


if __name__ == '__main__':
    # Создаём экземпляр класса Video
    video1 = Video('videoID1', 'Awesome video', 'https://www.youtube.com/watch?v=dQw4w9WgXcQ', 1000, 500)
    print(video1)  # Video('videoID1', 'Awesome video', 'https://www.youtube.com/watch?v=dQw4w9WgXcQ', 1000, 500)

    # Создаём экземпляр класса PLVideo
    pl_video1 = PLVideo('videoID2', 'Another awesome video', 'https://www.youtube.com/watch?v=3t6bLugtJkQ', 2000, 1200, 'playlistID1')
    print(pl_video1)  # PLVideo('videoID2', 'Another awesome video', 'https://www.youtube.com/watch?v=3t6bLugtJkQ', 2000, 1200, 'playlistID1')