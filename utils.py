# This file is part of PythonFO: Free virtual first officer for Microsoft Flight Simulator written entirely in Python
# Copyright (C) 2025  Vilgot Szasz Kero
# PythonFO comes with ABSOLUTELY NO WARRANTY; for details see COPYRIGHT.txt


# General settings
ptt_key = "alt"
enable_default_command = False # if True, the default command will be executed if no command prefix is recognized
default_command = "frequency"

# Speech recognition settings
recognizer_api = "google" # see "Supported speech recognition APIs" in "README.md"
whisper_model = "turbo"

# Demo mode (doesn't load SimConnect)
demo = False

# Developer mode (debug logs in console)
debug = True