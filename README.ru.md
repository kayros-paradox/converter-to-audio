# Инструкция по использованию

Необходимые пакеты: python3, pip3

### 1. Создание venv окружения в корневом каталоге.
python3 -m venv venv
### 2. Активация виртуального окружения проекта.
source venv/bin/activate
### 3. Установка необходимых модулей python3.
sh pip-sources.sh
### 4. Конвертация (пример):
python3 videotomp3.py \<videofile\> 
### 5. Проверить результат в папке audio.
cd audio

# Инструкция по установке

### 1. Создание venv окружения в корневом каталоге.
python3 -m venv venv
### 2. Активация виртуального окружения проекта.
source venv/bin/activate
### 3. Установка необходимых модулей python3.
sh pip-sources.sh
### 4. Установка pyinstaller.
pip3 install pyinstaller
### 5. Создание bin файла.
pyinstaller --onefile videotomp3.py
### 6. Проверить результат в папке audio.
cd audio

