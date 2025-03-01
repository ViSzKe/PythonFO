# This file is part of PythonFO: voice control for Microsoft Flight Simulator written entirely in Python
# Copyright (C) 2025  Vilgot Szasz Kero
# PythonFO comes with ABSOLUTELY NO WARRANTY; for details see COPYRIGHT.txt


from utils import debug
import keyboard
from listen_for_command import listen_for_command

# Define keys
PTT_KEY = "shift"  # PTT key

def main():
    print("Press " + PTT_KEY + " to talk.")
    while True:
        if keyboard.is_pressed(PTT_KEY):
            listen_for_command()

def license_notice():
    print("PythonFO  Copyright (C) 2025  Vilgot Szasz Kero")
    print("PythonFO comes with ABSOLUTELY NO WARRANTY; for details see COPYRIGHT.txt.")
    print("This is free software, and you are welcome to redistribute it")
    print("under certain conditions; see COPYRIGHT.txt for details.")
    print("")

if __name__ == "__main__":
    license_notice()
    main()
