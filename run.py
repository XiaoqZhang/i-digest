import argparse
from clipdigest.makegui import plot
from clipdigest.load_video import download
from clipdigest.audio2text import a2t
from clipdigest.get_compound import chem
from loguru import logger

def main():
    #parser = argparse.ArgumentParser()
    #parser.add_argument("-u", "--url", help="input the video link")
    #parser.add_argument("-f", "--file", help="give the audio file")
    #args = parser.parse_args()
    #if args.url is not None:
    #    download(args.url)
    #else:
    #    audio_file = args.file

    video_url , audio_path = plot()
    logger.debug(f"{audio_path}")
    video_text = a2t(audio_path)
    chem(video_text)


if __name__ == "__main__":
    main()
