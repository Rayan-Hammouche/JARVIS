import eel

eel.init("www")
eel.start('index.html', mode='edge', host='localhost', block=True)