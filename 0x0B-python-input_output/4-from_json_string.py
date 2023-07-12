#!/usr/bin/python3

"""
This code converts JSON to dictionaries
"""

import json


def from_json_string(my_str):
    """
    Returns an object that is a python data structure represented by a JSON stringx
    Args:
        -my_strin: str
    """
    return (json.loads(my_str))
