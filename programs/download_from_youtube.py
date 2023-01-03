from pytube import YouTube
from pytube.exceptions import PytubeError


def download_video(link: str, path: str):
    try:
        youtube_obj = YouTube(link)
        video = youtube_obj.streams.get_highest_resolution()
        video.download(path)
        return 'Done ✔'
    except PytubeError as pe:
        return f'Error: {pe}'


if __name__ == '__main__':
    link = input('Enter video link: ')
    path = 'videos/'
    print(download_video(link, path))
