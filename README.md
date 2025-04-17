from ai_response import friday_ai_response
import os
import speech_recognition as sr
import pyttsx3
import datetime

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)
engine.setProperty("rate", 200)

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

if __name__ == "__main__":
    while True:
        query = take_command()
        if "wake up" in query:
            from greetme import greetme
            greetme()

            while True:
                query = take_command()

                if "go to sleep" in query:
                    speak("Okay boss, going to sleep.")
                    break

                elif "hello" in query:
                    speak("Hello! How are you?")
                elif "i am fine" in query or "i am good" in query or "good" in query:
                    speak("That's good to hear!")
                elif "i am not good" in query or "i am sad" in query:
                    speak("Sorry to hear that. I'm here for you.")
                elif "how are you" in query:
                    speak("I am perfectly fine, thank you.")
                elif "thank you" in query:
                    speak("At your service!")
                elif "tell me something about yourself" in query:
                    speak("Hello! I am Edith, your AI assistant built with Python. I can answer your questions, generate content, and help you with daily tasks!")

                elif "make me a password" in query:
                    speak("Here is your password:")
                    from passwordgenerator import generate_password
                    generate_password()

                elif "check dns details" in query:
                    from tracer import fetch_dns_records, takeCommand
                    speak("Please tell me the domain name.")
                    domain_query = takeCommand()
                    if domain_query:
                        fetch_dns_records(domain_query)
                    else:
                        speak("I didn't catch that. Try again.")

                elif "play a game" in query:
                    from rockpaper import game_play
                    game_play()

                elif "google" in query:
                    from SEARCH import searchgoogle
                    searchgoogle(query)
                elif "youtube" in query:
                    from SEARCH import searchYoutube
                    searchYoutube(query)

                elif "what is the time" in query:
                    time = datetime.datetime.now().strftime("%H:%M")
                    speak(f"The time is {time}")

                elif "finally sleep" in query:
                    speak("Shutting down. Goodbye!")
                    exit()

                elif "tell me something" in query:
                    speak("Let me think...")
                    ai_response = friday_ai_response("Tell me something interesting.")
                    print(f"AI Response: {ai_response}")
                    speak(ai_response)

                elif "explain" in query or "define" in query or "what is" in query:
                    speak("Give me a second to explain that...")
                    ai_response = friday_ai_response(query)
                    print(f"AI Response: {ai_response}")
                    speak(ai_response)
