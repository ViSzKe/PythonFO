# This file is part of PythonFO: Free virtual first officer for Microsoft Flight Simulator written entirely in Python
# Copyright (C) 2025  Vilgot Szasz Kero
# PythonFO comes with ABSOLUTELY NO WARRANTY; for details see COPYRIGHT.txt


import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

from utils import debug, demo
if not demo:
    from simconnect import SimConnect
    sc = SimConnect()
from time import sleep


def flaps(flaps):
    if flaps == 0:
        flaps_str = "UP"
    elif flaps == 4:
        flaps_str = "DOWN"
    else:
        flaps_str = str(flaps)
    
    if demo:
        print("DEMO: command sent: FLAPS " + flaps_str)

    else:
        event_to_trigger = sc.send_event("FLAPS_" + flaps_str)
        for _ in range(3):
            event_to_trigger
            if debug:
                print("DEBUG: sc_functions.flaps: event sent: FLAPS_" + flaps_str)
            sleep(0.1)


def heading(heading):
    if " " in str(heading):
        heading = int(str(heading.replace(" ", "")))

    if demo:
        print("DEMO: command sent: HEADING " + str(heading))
    
    else:
        event_to_trigger = sc.send_event("A32NX.FCU_HDG_SET", int(heading))
        for _ in range(3):
            event_to_trigger
            if debug:
                print("DEBUG: sc_functions.heading: event sent: A32NX.FCU_HDG_SET, " + str(heading))
            sleep(0.1)


def frequency(frequency):
    # Add trailing zeroes
    while frequency < 100000000:
        frequency *= 10

    if demo:
        print("DEMO: command sent: FREQUENCY " + str(int(frequency/1000)))

    else:
        event_to_trigger = sc.send_event("COM_STBY_RADIO_SET_HZ", frequency)
        for _ in range(3):
            event_to_trigger
            if debug:
                print("DEBUG: sc_functions.frequency: event sent: COM_STBY_RADIO_SET_HZ, " + str(frequency))
            sleep(0.1)
