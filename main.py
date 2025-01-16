import eel
from playsound import playsound

# Playing Assistant Sound Function
def playAssistantSound():
    music_dir = "www\\assets\\audio\Audio.mp3"
    playsound(music_dir)

playAssistantSound()

eel.init("www")
eel.start('index.html', mode='edge', host='localhost', block=True)