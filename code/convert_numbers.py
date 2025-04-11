# This file is part of PythonFO: Free virtual first officer for Microsoft Flight Simulator written entirely in Python
# Copyright (C) 2025  Vilgot Szasz Kero
# PythonFO comes with ABSOLUTELY NO WARRANTY; for details see COPYRIGHT.txt


numbers_dict = {
    "zero": "0",
    "one": "1",
    "want": "1",
    "two": "2",
    "to": "2",
    "three": "3",
    "tree": "3",
    "four": "4",
    "for": "4",
    "five": "5",
    "six": "6",
    "sick": "6",
    "seven": "7",
    "eight": "8",
    "ate": "8",
    "light": "8",
    "nine": "9",
    "niner": "9",

    "fool": "full",
    "pool": "full",
}

def convert_numbers(string):
    for word, num in numbers_dict.items():
        string = string.replace(word, num)
    return string
