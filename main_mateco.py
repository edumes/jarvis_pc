import platform
import os
from mateco import TTS
import sys
from matplotlib.pyplot import text

username = os.getlogin()

jarvis = TTS()
jarvis.setup_voice('pt-br')

system = platform.system()
version = sys.getwindowsversion()[0]
build = platform.version().split('.')[2]

if __name__ == "__main__":
    jarvis.convert("bem vindo {} prazer em revê-lo".format(username))
    jarvis.speak()
    jarvis.convert("seu sistema {} {} está na build {}".format(system, version, build))
    jarvis.speak()