import platform
import os
from mateco import TTS
import sys
import pyttsx3
from matplotlib.pyplot import text

username = os.getlogin()
jarvis = pyttsx3.init('sapi5')


system = platform.system()
version = sys.getwindowsversion()[0]
build = platform.version().split('.')[2]
voices = jarvis.getProperty('voices')
jarvis.setProperty('voices', voices[0].id)

if __name__ == "__main__":
    jarvis.say("bem vindo {} prazer em revê-lo".format(username))
    jarvis.say("seu sistema {} {} está na build {}".format(system, version, build).upper())
    jarvis.runAndWait()







