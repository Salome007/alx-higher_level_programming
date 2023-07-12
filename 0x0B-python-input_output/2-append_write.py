#!/usr/bin/python3

def append_write(filename="", text=""):
    """
    Append text to the  end of afile, 
    and create if it doesnt exits.
    """

    """
    Append text to the end of file, and created if doesn't exists.
    Args:
      - filename: string
      - text: string
    """


     with open(filename, mode="a", encoding="utf-8") as _file:
        _file.write(text)

    return (len(text))

