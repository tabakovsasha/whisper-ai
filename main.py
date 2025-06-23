import whisper
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

# Загружаем модель (можно заменить на 'small', 'medium' или 'large' для большей точности)
model = whisper.load_model("large")

# Запрашиваем путь к видеофайлу у пользователя
video_path = input("Введите путь к видеофайлу: ")

# Транскрибируем файл целиком, явно указывая русский язык
result = model.transcribe(video_path, language="ru")

# Выводим текст
print(result["text"])