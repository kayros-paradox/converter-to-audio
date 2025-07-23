## 📄 Подготовительные шаги

### 1. Убедитесь, что у вас установлены пакеты python3 и python3-pip.

```bash
sudo apt install python3 -y
sudo apt install python3-pip -y
```

### 2. Создайте среду venv в вашем каталоге.

```bash 
python3 -m venv venv
```

<br />

## 💻 Простая установка

### 1. Активация виртуальной среды.
```bash
source venv/bin/activate
```

### 2. Установка необходимых модулей python3.
```bash
sh install.sh
```

### 3. Переместите их в /usr/bin [при желании] и используйте.
```bash
videotomp3 <video>
```

or 

```bash
./videotomp3 <video>
```

Результат выполнения находится в папке audio.

<br />

## 📖 Использовать без установки

### 1. Активация виртуальной среды.
```bash
source venv/bin/activate
```

### 2. Установка необходимых модулей python3.
```bash
sh pip-sources.sh
```

### 3. Использование (пример):
```python
python3 videotomp3.py <videofile>
```

Результат выполнения находится в папке audio.

