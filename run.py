import argparse
from clipdigest.load_video import download
from clipdigest.audio2text import a2t
from clipdigest.get_compound import chem

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--url", help="input the video link")
    parser.add_argument("-f", "--file", help="give the audio file")
    args = parser.parse_args()
    if args.url is not None:
        download(args.url)
        audio_file = "data/audio.mp4"
    else:
        audio_file = args.file

    video_text = a2t(audio_file)
    chem(video_text)


if __name__ == "__main__":
    main()
