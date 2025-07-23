## 📓 Instructions for use

### 1. Create a venv environment in your directory.
python3 -m venv venv
### 2. Activating the virtual environment.
source venv/bin/activate
### 3. Installation of the necessary modules python3.
sh pip-sources.sh
### 4. Conversion (example):
python3 videotomp3.py \<videofile\> 
### 5. Checking the result in the audio folder.
cd audio

<br/>

## 💻 Installation instructions

### 1. Create a venv environment in your directory.
python3 -m venv venv
### 2. Activating the virtual environment.
source venv/bin/activate
### 3. Installation of the necessary modules python3.
sh pip-sources.sh
### 4. Установка pyinstaller.
pip3 install pyinstaller
### 5. Создание bin файла.
pyinstaller --onefile videotomp3.py
### 6. Проверить результат в папке audio.
cd audio

