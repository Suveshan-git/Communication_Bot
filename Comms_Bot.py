import speech_recognition as sr
from gtts import gTTS
import os


r = sr.Recognizer()
print("Say Something: ")

with sr.Microphone() as source:
    audio_data = r.record(source, duration=5)
    print("Recognizing...")
    text = r.recognize_google(audio_data)
    print(text)

if text == "hello":
    response = "Hello! How are you?"
    language = "hi"
    output = gTTS(text=response, lang=language, slow=False)
    output.save("output.mp3")
    os.system("start output.mp3")
elif text == "what is your name":
    response = "my name is navishka"
    language = "hi"
    output = gTTS(text=response, lang=language, slow=False)
    output.save("output.mp3")
    os.system("start output.mp3")
else:
    response = "I do not have a response for that as yet."
    language = "hi"
    output = gTTS(text=response, lang=language, slow=False)
    output.save("output.mp3")
    os.system("start output.mp3")

