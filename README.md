# PythonFO v0.3.2-alpha

**Copyright (C) 2025  Vilgot Szasz Kero
PythonFO comes with ABSOLUTELY NO WARRANTY; for details see COPYRIGHT.txt**

## Development status

**Alpha**

## Introduction

This is a free, open-source virtual first officer for Microsoft Flight Simulator written entirely in Python. It uses SpeechRecognition (see **Supported speech recognition APIs** below) to transcribe commands, and pysimconnect to send data to the simulator.

*This is a personal project*, so it is obviously very limited compared to paid services. You also need to manually install the required packages (`pip install -r requirements.txt`) and run the script with your local Python.

## Requirements:

* Python (tested on 3.13.2) + requirements.txt + requirements_[optional feature].txt

## Supported simulators (tested on):

* Microsoft Flight Simulator 2020, 2024

## Supported aircraft (tested on):

* FlyByWire A32NX

## Supported speech recognition APIs:
* `google`: fast and light but less accurate, no additional requirements
* `whisper`: very slow and heavy but more accurate, requires `requirements_whisper.txt`

## Usage

1. Set your preferences in `utils.py`
2. Run `PythonFO.py`
3. Press the ptt key that you set in `utils.py` (no need to hold it down) and say your command (see `list_of_commands.md` for each aircraft)