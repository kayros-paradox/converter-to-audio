## 📄 Instructions for use

### 1. Create a venv environment in your directory.

```bash 
python3 -m venv venv
```

### 2. Activating the virtual environment.
```bash
source venv/bin/activate
```

### 3. Installation of the necessary modules python3.
```bash
sh pip-sources.sh
```

### 4. Conversion (example):
```python
python3 videotomp3.py \<videofile\>
```

### 5. Checking the result in the audio folder.
```bash
cd audio
```

<br/>

## 💻 Installation instructions

### 1. Create a venv environment in your directory.
```bash
python3 -m venv venv
```

### 2. Activating the virtual environment.
```bash
source venv/bin/activate
```

### 3. Installation of the necessary modules python3.
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
