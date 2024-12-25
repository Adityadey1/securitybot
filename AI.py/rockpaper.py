import pyttsx3
import speech_recognition
import random

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

def game_play():
    speak("Let's Play")
    print("Lets Playyyyyyyyyyyyyy!!")
    i = 0
    me_score = 0
    com_score = 0

    while(i<5):
        choose = ("rock", "paper", "scissor")
        com_choose = random.choice(choose)
        query = takeCommand().lower()
        if (query=="rock"):
            if(com_choose=="rock"):
                speak("roack")
                print(f"score:- me:- {me_score} : com;- {com_score}")
            elif(com_choose == "paper"):
                speak("paper")
                com_score += 1
                print(f"score:- me:- {me_score} : com;- {com_score}")
            else:
                speak("scissor")
                me_score +=1
                print(f"score:- me:- {me_score} : com;- {com_score}")
        if (query=="paper"):
            if(com_choose=="rock"):
                speak("roack")
                me_score +=1
                print(f"score:- me:- {me_score} : com;- {com_score}")
            elif(com_choose == "paper"):
                speak("paper")
                
                print(f"score:- me:- {me_score} : com;- {com_score}")
            else:
                speak("scissor")
                com_score +=1
                print(f"score:- me:- {me_score} : com;- {com_score}")
        elif (query=="scissor"or query=="ceasor"):
            if(com_choose=="rock"):
                speak("roack")
                com_score += 1
                print(f"score:- me:- {me_score} : com;- {com_score}")
            elif(com_choose == "paper"):
                speak("paper")
                me_score += 1
                print(f"score:- me:- {me_score} : com;- {com_score}")
            else:
                speak("scissor")
                # me_score +=1
                print(f"score:- me:- {me_score} : com;- {com_score}")
        i +=1
    print(f"final score:- me:- {me_score} : com:- {com_score}")

