#!/usr/bin/python3

def write_file(filename="", text=""):
    """
    This function writes in a file, if it doesnt exists, it creates one
    """
    with open(filename, mode="w", encoding="utf-8") as _file:
        _file.write(text)

    return (len(text))
