import os
import speech_recognition
import pyttsx3
import datetime
import requests

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)
engine.setProperty("rate",170)
rate = engine.setProperty("rate",300)

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


def alarm(query):
    timehere = open("alarmtext.txt", "a")
    timehere.write(query)
    timehere.close()
    os.startfile(alarm.py)


if __name__=="__main__":
    while True:
        query = takeCommand().lower()
        if "friday" in query:
            from greetme import greetme
            greetme()

            while True:
                query = takeCommand().lower()
                if "go to sleep" in query:
                    speak("ok boss")
                    
                elif "hello" in query:
                    speak("hello how are you?")
                elif "i am fine" in query:
                    speak("that's very good")
                elif "i am good" in query:
                    speak("that's good")
                elif "good" in query:
                    speak("that's good")
                elif "i am not good" in query:
                    speak("Feel sorry to hear that, I am here to help you")
                elif "i am sad" in query:
                    speak("Feel sorry to hear that, I am here to help you")
                elif "how r you" in query:
                    speak("i am perfectly fine sir")
                elif "thank you" in query:
                    speak("at your service sir")
                elif "tell me something about yourself" in query:
                    speak(" Hello! I am Friday, an advanced AI assistant created to help you with various tasks. I can process information, provide recommendations, and assist with problem-solving. My core functionality is built using Python, making me versatile and adaptable to different needs. Feel free to ask me anything, and I'll do my best to assist you!")              
                
                elif "make me a password" in query:
                    speak("here is your password")
                    from passwordgenerator import generate_password
                    generate_password()
                elif "check dns details" in query:
                    from tracer import fetch_dns_records, takeCommand
                    speak("Please tell me the domain name.")
                    domain_query = takeCommand()
                    if domain_query:
                        fetch_dns_records(domain_query)
                    else:
                        speak("I didn't catch the domain name. Please try again.")
            
                elif "play a game" in query:
                    from rockpaper import game_play
                    game_play()

                elif "google" in query:
                    from SEARCH import searchgoogle
                    searchgoogle(query)
                elif "youtube" in query:
                    from SEARCH import searchYoutube
                    searchYoutube(query)
                # elif "github" in query:
                    # from SEARCH import searchgithub
                    # searchgithub(query)
                elif "what is the time" in query:
                    time = datetime.datetime.now().strftime("%H:%M")
                    speak(f"the time is {time}")
                elif "finally sleep" in query:
                    speak("going off")
                    exit()




                    