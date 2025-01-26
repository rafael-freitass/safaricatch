# Importações de biblioteca
import os
import signal

# Importações de projeto
from modules.menu import menu 
from utils.timer import *

def main():
    # Inicia multiprocessing com timer
    timer_Main()
    if menu.main():
        # Encerra processo correndo em multiprocessing
        matar_Timer()
        # Encerra processo pai
        os.kill(os.getppid(), signal.SIGTERM)

if __name__ == "__main__":
    main()