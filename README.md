# PythonFO v0.3.0-alpha

**Copyright (C) 2025  Vilgot Szasz Kero
PythonFO comes with ABSOLUTELY NO WARRANTY; for details see COPYRIGHT.txt**

## Development status

**Alpha**

## Introduction

This is a free, open-source virtual first officer for Microsoft Flight Simulator written entirely in Python. It uses SpeechRecognition (select API in utils.py) to transcribe commands, and pysimconnect to send data to the simulator.

*This is a personal project*, so it is obviously very limited compared to paid services. You also need to manually install the required packages (`pip install -r requirements.txt`) and run the script with your local Python.

## Requirements:

* Python (tested on 3.13.2) + requirements.txt

## Supported simulators (tested on):

* Microsoft Flight Simulator 2020, 2024

## Supported aircraft (tested on):

* FlyByWire A32NX

## Usage

1. Set your preferences in `utils.py`
2. Run `PythonFO.py`
3. Press `shift` (no need to hold it down) and say your command (see **list of commands** below)

## List of commands

* flaps up, 1, 2, 3, 4 (full, down)
* heading 0-359 (example: "heading three-six-five", "heading one-nine")
* frequency 118.000-136.990 (example: "frequency one-two-two decimal eight", "frequency one-two-two-eight")