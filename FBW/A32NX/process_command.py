# This file is part of PythonFO: Free virtual first officer for Microsoft Flight Simulator written entirely in Python
# Copyright (C) 2025  Vilgot Szasz Kero
# PythonFO comes with ABSOLUTELY NO WARRANTY; for details see COPYRIGHT.txt


import sys
import os
sys.path.insert(1, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

import utils
import sc_functions
import re


def process_command(command):
    if utils.debug:
        print("DEBUG: process_command.process_command.command == " + command)

    if re.match(r"^(flaps|flap) \w+$", command) or (utils.enable_default_command and utils.default_command == "flaps" and len(command.split()) == 1):
        if utils.debug:
            print ("DEBUG: process_command.process_command: recognized flaps command")
        command_value = command.replace("flaps", "").strip()
        command_value = command_value.replace("flap", "").strip()
        if utils.debug:
            print("DEBUG: process_command.process_command: command_value == " + command_value)
        process_flaps(command_value)
        

    elif ("heading" in command and len(command.split()) == 2) or (utils.enable_default_command and utils.default_command == "heading" and len(command.split()) == 1 and re.match(r"^\d", command)):
        if utils.debug:
            print ("DEBUG: process_command.process_command: recognized heading command")
        command_value = command.replace("heading", "").strip()
        if utils.debug:
            print("DEBUG: process_command.process_command: command_value == " + command_value)
        process_heading(command_value)


    elif re.match(r"^frequency\s", command) or (utils.enable_default_command and utils.default_command == "frequency" and re.match(r"^\d", command)):
        if utils.debug:
            print("DEBUG: process_command.process_command: recognized frequency command")
        command_value = command.replace("frequency", "").strip()
        if utils.debug:
            print("DEBUG: process_command.process_command: command_value == " + command)
        process_frequency(command_value)

    
    else:
        print("Command not recognized.")


def process_flaps(command_value):
    flaps_dict = {
        "up": 0,
        "one": 1, "1": 1,
        "two": 2, "2": 2,
        "three": 3, "3": 3,
        "four": 4, "4": 4, "down": 4, "full": 4
    }
    flaps_int = flaps_dict.get(command_value, None)

    if utils.debug:
        print("DEBUG: process_command.process_flaps.flaps_int == " + str(flaps_int))

    if flaps_int is None:
        print("Invalid flaps value.")
        return

    sc_functions.flaps(flaps_int)


def process_heading(command_value):
    try:
        heading_int = int(command_value)
        if heading_int < 360:
            heading_int = f"{heading_int:03d}"
            if utils.debug:
                print("DEBUG: process_command.process_heading.heading_int == " + str(heading_int))
            sc_functions.heading(heading_int)
        else:
            print("Invalid heading value.")
    except ValueError:
        print("Invalid heading value.")


def process_frequency(command_value):
    frequency_str = str(command_value).replace("decimal", "").strip()
    frequency_str = str(frequency_str).replace(".", "").strip()
    frequency_int = int(frequency_str)

    if 118 <= frequency_int <= 136990 and len(frequency_str) <= 6:
        if utils.debug:
            print("DEBUG: process_command.process_frequency.frequency_str == " + str(frequency_str))
            print("DEBUG: process_command.process_frequency.frequency_int == " + str(frequency_int))
        sc_functions.frequency(frequency_int)
    else:
        print("Invalid frequency value.")