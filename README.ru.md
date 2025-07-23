## 📄 Инструкция по использованию

Необходимые пакеты: python3, pip3

### 1. Создание venv окружения в корневом каталоге.
```bash
python3 -m venv venv
```

### 2. Активация виртуального окружения проекта.
```bash
source venv/bin/activate
```

### 3. Установка необходимых модулей python3.
```bash
sh pip-sources.sh
```

### 4. Конвертация (пример):
```bash
python3 videotomp3.py <videofile>
```

### 5. Проверить результат в папке audio.
```bash
cd audio
```

<br />

## 💻 Инструкция по установке

### 1. Создание venv окружения в корневом каталоге.
```bash
python3 -m venv venv
```

### 2. Активация виртуального окружения проекта.
```bash
source venv/bin/activate
```

### 3. Установка необходимых модулей python3.
```bash
sh pip-sources.sh
```

### 4. Установка pyinstaller.
```bash
pip3 install pyinstaller
```

### 5. Создание bin файла.
```bash
pyinstaller --onefile videotomp3.py
```

### 6. Проверить результат в папке audio.
```bash
cd audio
```

