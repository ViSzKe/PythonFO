# This file is part of PythonFO: Free virtual first officer for Microsoft Flight Simulator written entirely in Python
# Copyright (C) 2025  Vilgot Szasz Kero
# PythonFO comes with ABSOLUTELY NO WARRANTY; for details see COPYRIGHT.txt


# General settings
ptt_key = "shift"
enable_default_command = False # If True, the default command will be executed if no command prefix is recognized
default_command = "frequency"

# Speech recognition settings
recognizer_api = "google" # google: fast and light but less accurate, whisper: slow and heavy but more accurate
whisper_model = "turbo"

# Developer mode
debug = True