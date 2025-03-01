# This file is part of PythonFO: voice control for Microsoft Flight Simulator written entirely in Python
# Copyright (C) 2025  Vilgot Szasz Kero
# PythonFO comes with ABSOLUTELY NO WARRANTY; for details see COPYRIGHT.txt


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
        command = recognizer.recognize_google(audio)
        print(f"Recognized: {command}")
        process_command(command)
    except sr.UnknownValueError:
        print("Could not understand the command.")
    except sr.RequestError:
        print("Could not request results.")