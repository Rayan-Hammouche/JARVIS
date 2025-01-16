import eel
from engine.features import playAssistantSound

eel.init("www")

@eel.expose
def play_sound():
    playAssistantSound()

eel.start('index.html', mode='edge', host='localhost', block=True)