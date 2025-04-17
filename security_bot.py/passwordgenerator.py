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


 
def generate_password(length=12):
    # Define the character sets to use in the password
    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    digits = string.digits
    special_characters = string.punctuation

    # Ensure the password contains at least one character from each set
    password = [
        random.choice(uppercase),
        random.choice(lowercase),
        random.choice(digits),
        random.choice(special_characters)
    ]

    # Fill the rest of the password length with random choices from all sets
    all_characters = uppercase + lowercase + digits + special_characters
    password += random.choices(all_characters, k=length-4)

    # Shuffle the list to ensure randomness and then join to form the final password string
    random.shuffle(password)
    return ''.join(password)

# Example usage
password = generate_password(12)
print(f"Generated password: {password}")