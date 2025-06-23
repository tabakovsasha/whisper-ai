import glob
import whisper
import ssl
import os

ssl._create_default_https_context = ssl._create_unverified_context

model = whisper.load_model("small")

device_choice = input("Выберите устройство для обработки (cpu/gpu): ").strip().lower()
if device_choice not in ['cpu', 'gpu']:
    print("Неверный выбор. Допустимые значения: cpu или gpu.")
    exit()

device = "cuda" if device_choice == "gpu" else "cpu"

media_files = glob.glob("./*.*")
media_files = [f for f in media_files if f.lower().endswith(('.mp4', '.mp3', '.wav', '.m4a'))]

if not media_files:
    print("В текущей папке не найдено подходящих медиафайлов.")
    exit()

print("Доступные медиафайлы:")
for i, file in enumerate(media_files):
    print(f"{i + 1}: {file}")

choice = input("Введите номер файла, который хотите транскрибировать: ")

try:
    index = int(choice) - 1
    video_path = media_files[index]
except (ValueError, IndexError):
    print("Неверный выбор.")
    exit()

try:
    result = model.transcribe(video_path, language="ru", device=device)
    print(result["text"])
    base_name = os.path.splitext(os.path.basename(video_path))[0]
    output_filename = f"{base_name}_transcription.txt"
    with open(output_filename, "w", encoding="utf-8") as f:
        f.write(result["text"])
    print(f"Транскрипция сохранена в файл: {output_filename}")
except Exception as e:
    print(f"Ошибка при транскрипции: {e}")