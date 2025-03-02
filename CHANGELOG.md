# New features in 0.2.0
* You can now change the PTT key in utils.py
* New speech recognition model: OpenAI Whisper
* You can now choose your preferred speech recognition model (Google or Whisper) in utils.py
* You can now say only the last number(s) in a heading and zeroes will be added automatically, for example "heading one-nine" instead of "heading zero-one-nine"

# Technical changes in 0.2.0
* utils.py moved to project root
* Add a sleep(0.1) to the main loop to reduce CPU usage
* Add a "Recognizing..." message to the console to indicate that the recording is completed and the speech recognition is in progress (this is especially useful for Whisper)
* Add code to remove spaces/punctuation/special characters that speech recognition (specifically Whisper) sometimes adds
* Add a safeguard against trying to command frequencies longer than 6 digits