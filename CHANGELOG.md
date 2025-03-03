# New features in 0.3.0
* You can now set a default command in utils.py. If no prefix is added when you say your command, the program will interpret it as the default command. This is useful for commands that you use frequently.

# Technical changes in 0.3.0
* process_command() now removes the specific prefix (flaps/heading/frequency) before sending it to the appropriate processing function. This should increase reliability and enable for more complex processing functions.

# Licensing changes in 0.3.0
* PythonFO description changed from: "voice control for Microsoft Flight Simulator written entirely in Python" to "Free virtual first officer for Microsoft Flight Simulator written entirely in Python"