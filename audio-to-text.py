import os
import sys
import argparse
import questionary
import wave
from contextlib import contextmanager

OUTSRC = 'texts'


@contextmanager
def suppress_stdout():
    original_stdout = sys.stdout
    sys.stdout = open(os.devnull, 'w')
    try:
        yield
    finally:
        sys.stdout.close()
        sys.stdout = original_stdout


def isNotTextFileExists(src):
    if os.path.exists(src):
        return questionary.confirm(
                'Файл {src} уже существует. Вы хотите перезаписать его?'
        ).ask()
    else:
        return True


# Конвертация аудио в текстовый файл (формат: txt).
def convertToText(src='audio.wav'):
    # TODO: дописать.


# Проверка расширения аудио файла.
def isAudio(src='source'):
    try:
        print(f'Обрабатываем файл: {src}')

        with suppress_stdout():
            wf = wave.open(src, "rb")
            wf.close()

        return True
    except Exception as e:
        print(f'{src} не является аудиофайлом или ошибка выполнения: {e}')
        return False


# Конвертирование аудио файлов.
def convert(src):
    if os.path.exists(src):
        if isAudio(src):
            convertToText(src)
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
