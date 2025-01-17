import pyttsx3

def speak(text, voice_id=2):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[voice_id].id)
    engine.setProperty('rate', 174)
    print(f"Using voice: {voices[voice_id].name}")
    engine.say(text)
    engine.runAndWait()

# Example usage
speak("Hello, I am your virtual assistant", voice_id=2)