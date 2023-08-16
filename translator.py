from googletrans import Translator

translator = Translator()


with open("C:\\Users\\dell\\PycharmProjects\\pythonProject5\\есенин.txt", "r", encoding="cp1251") as file:
    original_text = file.read()

translated_text = translator.translate(original_text, dest="en").text

with open("C:\\Users\\dell\\PycharmProjects\\pythonProject5\\есенин в переводе.txt", "w", encoding="cp1251") as file:

    file.write(translated_text)

print("Файл с переведенным текстом создан")