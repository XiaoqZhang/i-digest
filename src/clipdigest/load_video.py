from pytube import YouTube
from loguru import logger

def download(link):
    try:
        yt=YouTube(link)
    except:
        print('Connection error')

    yt.streams.filter(file_extension='mp4')
    stream=yt.streams.get_by_itag(139)
    logger.info("Downloading the audio")
    stream.download('data',"audio.mp4")