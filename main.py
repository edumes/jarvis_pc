import platform
import os
import sys
import pyttsx3
from matplotlib.pyplot import text

username = os.getlogin()
jarvis = pyttsx3.init()
voices = jarvis.getProperty('voices')      
jarvis.setProperty('voice', voices[3].id)

system = platform.system()
version = sys.getwindowsversion()[0]
build = platform.version().split('.')[2]

speech = str("seu sistema {} {} está na build {}".format(system, version, build).upper())

jarvis.say("bem vindo {} prazer em revê-lo".format(username))
jarvis.say(speech)


jarvis.runAndWait()







