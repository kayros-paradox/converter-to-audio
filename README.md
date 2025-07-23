# Инструкция по использованию

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
