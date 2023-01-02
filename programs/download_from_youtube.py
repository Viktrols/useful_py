from pytube import YouTube
from pytube.exceptions import PytubeError


def download_video(link: str, path: str):
    try:
        youtube_obj = YouTube(link)
        video = youtube_obj.streams.get_highest_resolution()
        video.download(path)
        return 'Done ✔'
    except PytubeError as pe:
        return f'{pe}'


if __name__ == '__main__':
    link = input('Введите ссылку на видео: ')
    path = 'videos/'
    print(download_video(link, path))
