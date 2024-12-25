import speech_recognition
import pyttsx3
import pywhatkit
import wikipedia
import webbrowser
# import github
def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        r.energy_threshold = 400
        audio = r.listen(source,0,4)
    try:
        print("understand...")
        query = r.recognize_google(audio,language='en-in')
        print(f"you said: {query}\n")

    except Exception:
        print("say that again")
        return "none"
    return query
query = takeCommand().lower()

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)
engine.setProperty("rate",170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def searchgoogle(query):
    if "google" in query:
        import wikipedia as googleScrap
        query = query.replace("friday","")
        query = query.replace("google search","")
        query = query.replace("google","")
        speak("this is what i found on google")

        try:
            pywhatkit.search(query)
            result = googleScrap.summary(query,1)
            speak(result)
        except:
            speak("nothing found")

def searchYoutube(query):
    if "youtube" in query:
        # import wikipedia as googleScrap
        query = query.replace("friday","")
        query = query.replace("youtube search","")
        query = query.replace("youtube","")
        web = "https://www.youtube.com/results?search_query="+ query
        webbrowser.open(web)
        pywhatkit.playonyt(query)
        speak("this is what i found on youtube")


    else:
        speak("nothing found")

def searchgithub(query):
    if "open github" in query:
        query = query.replace("github","")
        query = query.replace("github search","")
        query = query.replace("friday","")
        web = "https://github.com/"+ query
        speak("from github...")
        webbrowser.open (web)
        pywhatkit.search(query)
        result = github.summary(query, sentence = 2)
        print(result)
        speak(result)


 
        



