import os
import sys
import argparse
import questionary
from contextlib import contextmanager
from moviepy import VideoFileClip

OUTSRC = 'audio'


# Hiding output via context.
@contextmanager
def suppress_stdout():
    original_stdout = sys.stdout
    sys.stdout = open(os.devnull, 'w')
    try:
        yield
    finally:
        sys.stdout.close()
        sys.stdout = original_stdout


# Checking file existence.
def isNotAudioExists(src):
    if os.path.exists(src):
        return questionary.confirm(
                'The file {src} already exists. Do you want to overwrite it?'
        ).ask()
    else:
        return True


# Convert video to audio file (format mp3).
def convertToAudio(src='video.mp4'):
    with suppress_stdout():
        video = VideoFileClip(src)
        audio = video.audio
        audio.nschannels = 2

    # Extract audio.
    basesrc = os.path.basename(src)
    filename = os.path.splitext(basesrc)[0]
    audioSrc = f'{OUTSRC}/{filename}.mp3'
    if isNotAudioExists(audioSrc):
        audio.write_audiofile(
                filename=audioSrc,
                nbytes=2,
                bitrate='320k'
        )

    # Close.
    audio.close()
    video.close()


# Checking video file extension.
def isVideo(src='source'):
    try:
        print(f'Processing file: {src}')

        with suppress_stdout():
            clip = VideoFileClip(src)
            clip.close()  # Closed the clip if it was successfully opened.
        return True
    except Exception as e:
        print(f'{src} is not a video file or runtime error: {e}')
        return False


# Converting video files.
def convert(src):
    if os.path.exists(src):
        if isVideo(src):
            convertToAudio(src)
    else:
        print(f'{src}: File does not exist')


def createDir():
    try:
        os.makedirs(OUTSRC, exist_ok=True)
        return True
    except Exception as e:
        print(f'Unable to save data. Possible permission error: {e}')
        return False


def main(files):
    if createDir():
        print('Processing file list.')

        for file in files:
            convert(file)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Processing file list.')
    parser.add_argument('files', nargs='+', help='List of files to process')

    args = parser.parse_args()
    main(args.files)
