from playsound import playsound
import eel

# Playing Assistant Sound Function

@eel.expose
def playAssistantSound():
    music_dir = "www\\assets\\audio\Audio.mp3"
    playsound(music_dir)