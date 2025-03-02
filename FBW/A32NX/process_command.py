# This file is part of PythonFO: voice control for Microsoft Flight Simulator written entirely in Python
# Copyright (C) 2025  Vilgot Szasz Kero
# PythonFO comes with ABSOLUTELY NO WARRANTY; for details see COPYRIGHT.txt


import sys
import os
sys.path.insert(1, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from utils import debug
import sc_functions
import re


def process_command(command):
    if debug:
        print("DEBUG: process_command.process_command.command == " + command)

    if re.match(r"^(flaps|flap) \w+$", command):
        if debug:
            print ("DEBUG: process_command.process_command: recognized flaps command")
        process_flaps(command)
        

    elif "heading" in command and len(command.split()) == 2:
        if debug:
            print ("DEBUG: process_command.process_command: recognized heading command")
        process_heading(command)


    elif re.match(r"^frequency\s", command):
        if debug:
            print("DEBUG: process_command.process_command: recognized frequency command")
        process_frequency(command)

    
    else:
        print("Command not recognized.")


def process_flaps(command):
    flaps_dict = {
        "up": 0,
        "one": 1, "1": 1,
        "two": 2, "2": 2,
        "three": 3, "3": 3,
        "four": 4, "4": 4, "down": 4, "full": 4
    }
    flaps_str = command.split()[1]
    flaps_int = flaps_dict.get(flaps_str, None)

    if debug:
        print("DEBUG: process_command.process_flaps.flaps_str == " + str(flaps_str))
        print("DEBUG: process_command.process_flaps.flaps_int == " + str(flaps_int))

    if flaps_int is None:
        print("Invalid flaps value.")
        return

    sc_functions.flaps(flaps_int)


def process_heading(command):
    heading_str = command.split()[1]
    if debug:    
        print("DEBUG: process_command.process_heading.heading_str == " + str(heading_str))

    try:
        heading_int = int(heading_str)
        if heading_int < 360:
            heading_int = f"{heading_int:03d}"
            if debug:
                print("DEBUG: process_command.process_heading.heading_int == " + str(heading_int))
            sc_functions.heading(heading_int)
        else:
            print("Invalid heading value.")
    except ValueError:
        print("Invalid heading value.")


def process_frequency(command):
    frequency_str = str(command).replace(" decimal ", "")
    frequency_str = str(frequency_str).replace(".", "")
    frequency_str = str(frequency_str).split()[1]
    frequency_int = int(frequency_str)

    if 118 <= frequency_int <= 136990 and len(frequency_str) <= 6:
        if debug:
            print("DEBUG: process_command.process_frequency.frequency_str == " + str(frequency_str))
            print("DEBUG: process_command.process_frequency.frequency_int == " + str(frequency_int))
        sc_functions.frequency(frequency_int)
    else:
        print("Invalid frequency value.")