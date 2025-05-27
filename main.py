import whisper
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

# Загружаем модель (можно заменить на 'small', 'medium' или 'large' для большей точности)
model = whisper.load_model("turbo")

# Задаём путь к видеофайлу
video_path = "/Users/atabakov/Yandex.Disk.localized/ntechlab-work/Пулково/2025-05-27_14-48-17.mp4"

# Транскрибируем файл целиком, явно указывая русский язык
result = model.transcribe(video_path, language="ru")

# Выводим текст
print(result["text"])