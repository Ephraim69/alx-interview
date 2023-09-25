#!/usr/bin/python3
"""UTF-8 Validation"""


def validUTF8(data):
    """
    Determines a valid UTF-8 encoding
    """
    return not any(
        byte >> 7 != 0
        and byte >> 5 != 0b110
        and byte >> 4 != 0b1110
        and byte >> 3 != 0b11110
        for byte in data
    )
