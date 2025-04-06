# This file is part of PythonFO: Free virtual first officer for Microsoft Flight Simulator written entirely in Python
# Copyright (C) 2025  Vilgot Szasz Kero
# PythonFO comes with ABSOLUTELY NO WARRANTY; for details see COPYRIGHT.txt


import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../code")))

from utils import ptt_key
import keyboard
from listen_for_command import listen_for_command
from process_command import process_command
from time import sleep

from license_notice import license_notice

def main():
    print("Press " + ptt_key + " to talk.")
    while True:
        if keyboard.is_pressed(ptt_key):
            command = listen_for_command()
            if command == "error":
                continue
            else:
                process_command(command)

        sleep(0.1)

if __name__ == "__main__":
    license_notice()
    main()