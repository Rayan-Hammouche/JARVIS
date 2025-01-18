import pyttsx3
import speech_recognition as sr

def speak(text, voice_id=2):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[voice_id].id)
    engine.setProperty('rate', 174)
    print(f"Using voice: {voices[voice_id].name}")
    engine.say(text)
    engine.runAndWait()

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print("Sorry, I did not catch that. Could you please repeat?")
        return ""
    
    return query.lower()

# Example usage
if __name__ == "__main__":
    text = take_command()
    if text:
        speak(text, voice_id=2)