import requests
import json

def text_to_speech(filename):
    with open(filename, 'r') as file:
        text = file.read()
    headers = {"Authorization": f"Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiYzY0MmUzMjgtODNhYi00NjhjLTkxZDAtNDc3YjA5NzZhNzhjIiwidHlwZSI6ImZyb250X2FwaV90b2tlbiJ9.aM5uf11zWsQ6_MGCVS9eV4u014hP8MZTm8z8E3qpuv0"}
    url = 'https://api.edenai.run/v2/audio/text_to_speech'

    payload = {
        'providers':'google',
        'language':'en-US',
        'option':'MALE',
        'google':'en-US-Neural2-F',
        'text':f'{text}'
    }
    response = requests.post(url, json=payload, headers=headers)
    result = json.loads(response.text)

    audio_url = result.get('google').get('audio_resource_url')
    r = requests.get(audio_url)

    with open(f'есенинозвучка.wav', 'wb') as file:
        file.write(r.content)

def main():
    text_to_speech(filename='C:\\Users\\dell\\PycharmProjects\\pythonProject5\\есенинвпереводе.txt')

if __name__ == '__main__':
    main()