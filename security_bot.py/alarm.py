import pyttsx3
import datetime
import os

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)
engine.setProperty("rate",170)
rate = engine.setProperty("rate",300)

def speak(audio):
    engine.say(audio)
    engine.runAndWait() 

extractedtime = open("alarmtext.txt", "rt")
time = extractedtime.read()
time = str(time)
extractedtime.close()

deletetime = open("alarmtext.txt", "r+")
deletetime.truncate(0)
deletetime.close()

def ring(time):
    timeset = str(time)
    timenow = timeset.replace("friday")
    timenow = timenow.replace("set an alarm","")
    alarmtime = str(timenow)
    print(alarmtime)
    while True:
        currenttime = datetime.datetime.now().strftime("%H,%M,%S")
        if currenttime == alarmtime:
            speak("alarm ringing")
            os.startfile("music.mp3")
            
