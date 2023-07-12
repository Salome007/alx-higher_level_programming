#!/usr/bin/python3

def append_write(filename="", text=""):
    """
    Append text to the  end of afile, and create if it doesnt exits.
    """
    with open(filename, mode="a", encoding="utf-8") as _file:
        _file.write(text)

    return (len(text))

