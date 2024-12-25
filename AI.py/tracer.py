import speech_recognition as sr
import dns.resolver
import pyttsx3

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

def fetch_dns_records(domain):
    records_type = ['A', 'AAAA', 'CNAME', 'MX', 'TXT', 'SOA']
    resolver = dns.resolver.Resolver()
    
    speak(f"Fetching DNS records for {domain}")
    print(f"\nFetching DNS records for: {domain}\n")
    for record_type in records_type:
        try:
            answer = resolver.resolve(domain, record_type)
            print(f'{record_type} records for {domain}:')
            speak(f"{record_type} records found for {domain}")
            for data in answer:
                print(f' {data}')
                speak(str(data))
        except dns.resolver.NoAnswer:
            continue
        except dns.resolver.NXDOMAIN:
            speak(f"The domain {domain} does not exist.")
            print(f"Error: The domain {domain} does not exist.")
            break
        except Exception as e:
            speak("An error occurred while fetching DNS records.")
            print(f"An error occurred: {e}")
            break

def main():
    speak("Hello! Say 'fetch DNS records' to start.")
    while True:
        query = takeCommand()
        
        if "fetch dns records" in query:
            speak("Please tell me the domain name.")
            domain_query = takeCommand()
            if domain_query:
                fetch_dns_records(domain_query)
            else:
                speak("I didn't catch the domain name. Please try again.")
        
        elif "exit" in query or "stop" in query:
            speak("Goodbye!")
            break

if __name__ == "__main__":
    main()
