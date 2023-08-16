import ffmpeg
from pydub import AudioSegment

def convert_mp3_to_wav(mp3_file, wav_file):
    sound = AudioSegment.from_mp3(mp3_file)
    sound.export(wav_file, format="wav")

mp3_path = "C:\\Users\\dell\\PycharmProjects\\pythonProject5\\Есенин.mp3"
wav_path = "C:\\Users\\dell\PycharmProjects\\pythonProject5\\Есенин.wav"

if not mp3_path.lower().endswith(".mp3"):
    print("файл должен иметь расширение .mp3")
    exit()

if not wav_path.lower().endswith(".wav"):
    print("файл должен иметь расширение .wav")
try:
    convert_mp3_to_wav(mp3_path, wav_path)
except Exception as e:
    print("Ошибка при конвертации mp3 в wav:",e)


