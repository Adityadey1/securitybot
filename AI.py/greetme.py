import pyttsx3
import datetime

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate',170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def greetme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("hi, Good Morning sir")
    elif hour>12 and hour<=18:
        speak("hi, Good Afternoon sir")
    else:
        speak("hi, good evening sir")

    speak("I am friday. How can I help you")
