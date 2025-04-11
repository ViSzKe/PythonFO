# This file is part of PythonFO: Free virtual first officer for Microsoft Flight Simulator written entirely in Python
# Copyright (C) 2025  Vilgot Szasz Kero
# PythonFO comes with ABSOLUTELY NO WARRANTY; for details see COPYRIGHT.txt


import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from utils import recognizer_api
if recognizer_api == "vosk":
    import vosk, json
    vosk.SetLogLevel(-1)
    from utils import vosk_model as vosk_model_name
    vosk_model = vosk.Model(vosk_model_name)

from convert_numbers import convert_numbers

from time import sleep

import speech_recognition as sr
recognizer = sr.Recognizer()
if recognizer_api == "vosk":
    mic = sr.Microphone(sample_rate=16000)
else:
    mic = sr.Microphone()


def listen_for_command():
    with mic as source:
        try:
            print("Listening...")
            #recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source, timeout=10)
        except sr.WaitTimeoutError:
            print("Couldn't hear anything")
            return "error"

    try:
        if recognizer_api == "google":
            print("Recognizing...")
            command = recognizer.recognize_google(audio)
            if command is None:
                raise ValueError("Recognzer returned None")

        elif recognizer_api == "vosk":
            print("Recognizing...")
            command = recognize_vosk(audio)

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
        
        command = convert_numbers(command)

        print(f"Recognized: {command}")
        return command
    
    except sr.UnknownValueError:
        print("Could not understand the command.")
        return "error"
    except sr.RequestError:
        print("Could not request results.")
        return "error"


def recognize_vosk(audio):
    raw_data = audio.get_raw_data()
    vosk_recognizer = vosk.KaldiRecognizer(vosk_model, 16000)
    vosk_recognizer.SetWords(True)

    chunk_size = 4096
    for i in range(0, len(raw_data), chunk_size):
        chunk = raw_data[i:i+chunk_size]
        if vosk_recognizer.AcceptWaveform(chunk):
            break

    result = json.loads(vosk_recognizer.FinalResult())
    del vosk_recognizer
    return result.get("text", "").strip()