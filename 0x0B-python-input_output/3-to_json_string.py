#!/usr/bin/python3
"""
This code converts dictionaries to JSON
"""


import JSON


def to_json_string(my_obj):
    """
    convert a dictionary to JSON format
    Args:
    -my_object: dict
    """

    return (json.dumps(my_obj))
