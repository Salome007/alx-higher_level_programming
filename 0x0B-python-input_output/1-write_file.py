#!/usr/bin/python3
"""
This function reads files
"""

def read_file(filename=""):
    """
    This function reads a file and print its content
    """
    with open(filename, encoding="utf-8") as _file:
        print(_file.read(), end="")
