# This file is part of PythonFO: Free virtual first officer for Microsoft Flight Simulator written entirely in Python
# Copyright (C) 2025  Vilgot Szasz Kero
# PythonFO comes with ABSOLUTELY NO WARRANTY; for details see COPYRIGHT.txt


import sys
import os
sys.path.insert(1, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from utils import recognizer_api
if recognizer_api == "whisper":
    from utils import whisper_model

from time import sleep

import speech_recognition as sr
recognizer = sr.Recognizer()
mic = sr.Microphone()

from process_command import process_command


def listen_for_command():
    with mic as source:
        print("Listening...")
        #recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        if recognizer_api == "whisper":
            print("Recognizing...")
            command = recognizer.recognize_whisper(audio, model=whisper_model)
            if command is None:
                raise ValueError("Recognzer returned None")

        elif recognizer_api == "google":
            print("Recognizing...")
            command = recognizer.recognize_google(audio)
            if command is None:
                raise ValueError("Recognzer returned None")

        else:
            raise ValueError("Invalid recognizer API")
        
        command = command.lower()
        if command.startswith(" "):
            command = command[1:]
        if command.endswith((".", "!", "?")):
            command = command[:-1]
        if "-" in command:
            command = command.replace("-", "")
        if "," in command:
            command = command.replace(",", "")
        if "/" in command:
            command = command.replace("/", "")
        
        print(f"Recognized: {command}")
        process_command(command)
    
    except sr.UnknownValueError:
        print("Could not understand the command.")
    except sr.RequestError:
        print("Could not request results.")