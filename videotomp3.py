import os
import sys
import argparse
import questionary
from contextlib import contextmanager
from moviepy import VideoFileClip

OUTSRC = 'audio'


# Скрытие вывода через контекст.
@contextmanager
def suppress_stdout():
    original_stdout = sys.stdout
    sys.stdout = open(os.devnull, 'w')
    try:
        yield
    finally:
        sys.stdout.close()
        sys.stdout = original_stdout


# Проверка существования файла.
def isNotAudioExists(src):
    if os.path.exists(src):
        return questionary.confirm(
                'Файл {src} уже существует. Вы хотите перезаписать его?'
        ).ask()
    else:
        return True


# Конвертация видео в аудиофайл (формат: mp3).
def convertToAudio(src='video.mp4'):
    with suppress_stdout():
        video = VideoFileClip(src)
        audio = video.audio
        audio.nschannels = 2

    # Извлечение audio.
    basesrc = os.path.basename(src)
    filename = os.path.splitext(basesrc)[0]
    audioSrc = f'{OUTSRC}/{filename}.mp3'
    if isNotAudioExists(audioSrc):
        audio.write_audiofile(
                filename=audioSrc,
                nbytes=2,
                bitrate='320k'
        )

    # Закрытие.
    audio.close()
    video.close()


# Проверка расширения видео файла.
def isVideo(src='source'):
    try:
        print(f'Обрабатываем файл: {src}')

        with suppress_stdout():
            clip = VideoFileClip(src)
            clip.close()  # Закрываем клип, если он успешно открыт
        return True
    except Exception as e:
        print(f'{src} не является видеофайлом или ошибка выполнения: {e}')
        return False


# Конвертирование видео файлов.
def convert(src):
    if os.path.exists(src):
        if isVideo(src):
            convertToAudio(src)
    else:
        print(f'{src}: Файл не существует')


def createDir():
    try:
        os.makedirs(OUTSRC, exist_ok=True)
        return True
    except Exception as e:
        print(f'Невозможно сохранить данные. Возможно ошибка разрешений: {e}')
        return False


def main(files):
    if createDir():
        print('Обработка списка файлов.')

        for file in files:
            convert(file)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Обработка списка файлов.')
    parser.add_argument('files', nargs='+', help='Список файлов для обработки')

    args = parser.parse_args()
    main(args.files)
