# New features in 0.3.1
* Whisper's requirements are now separated from the main requirements, so you can install them only if you want to use Whisper.

# Bug fixes in 0.3.1
* Frequency commands did not work if "decimal" was in the command.

# Other changes in 0.3.1
* Zero padding for headings is now removed, because different users might want to add zeroes before or after the commanded numbers.
* The default ptt key is now `alt`.
* Every aircraft now as its own `list_of_commands.md` in its folder.

# Technical changes in 0.3.1
* `listen_for_commands.py` is now separated from the aircraft-specific code, because the same speech recognition code can be used regardless of aircraft. This should make it easier to add more supported aircraft.