import random
import string
import pyttsx3
import speech_recognition

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)
engine.setProperty("rate",170)
rate = engine.setProperty("rate",170)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def take_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.pause_threshold = 1  
        recognizer.energy_threshold = 200  
        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=8)  
            return recognizer.recognize_google(audio, language='en-in').lower()
        except (sr.WaitTimeoutError, sr.UnknownValueError):
            print("Listening timed out or unclear speech.")
            return ""
        except sr.RequestError:
            print("Check internet connection.")
            return ""

