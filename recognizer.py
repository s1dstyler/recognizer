import speech_recognition as sr

def convert_wav_to_text(wav_path):
    r = sr.Recognizer()


    with sr.AudioFile(wav_path) as source:
        audio_data = r.record(source)
        r.adjust_for_ambient_noise(source, duration=5)
        text = r.recognize_google(audio_data, language="ru")

    with open("есенин.txt", "w") as file:
        file.write(text)

wav_path = "C:\\Users\\dell\\PycharmProjects\\pythonProject5\\Есенин.wav"

convert_wav_to_text(wav_path)
