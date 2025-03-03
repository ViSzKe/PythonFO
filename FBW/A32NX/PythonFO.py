# This file is part of PythonFO: Free virtual first officer for Microsoft Flight Simulator written entirely in Python
# Copyright (C) 2025  Vilgot Szasz Kero
# PythonFO comes with ABSOLUTELY NO WARRANTY; for details see COPYRIGHT.txt


import sys
import os
sys.path.insert(1, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from utils import debug, ptt_key
import keyboard
from listen_for_command import listen_for_command
from time import sleep

def main():
    print("Press " + ptt_key + " to talk.")
    while True:
        if keyboard.is_pressed(ptt_key):
            listen_for_command()
        sleep(0.1)

def license_notice():
    print("PythonFO  Copyright (C) 2025  Vilgot Szasz Kero")
    print("PythonFO comes with ABSOLUTELY NO WARRANTY; for details see COPYRIGHT.txt.")
    print("This is free software, and you are welcome to redistribute it")
    print("under certain conditions; see COPYRIGHT.txt for details.")
    print("")

if __name__ == "__main__":
    license_notice()
    main()