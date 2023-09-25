#!/usr/bin/python3
"""
Module for UTF-8 validation
"""


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.

    Args:
        data (list of int): Each integer represents 1 byte of data, 
                            only the 8 least significant bits are considered.

    Returns:
        bool: True if data is a valid UTF-8 encoding, else False.
    """
    num_bytes = 0  # Number of bytes in a UTF-8 character

    # Mask to check the first bit in a byte
    mask1 = 1 << 7
    # Mask to check the second bit in a byte
    mask2 = 1 << 6

    for num in data:
        mask = 1 << 7
        if num_bytes == 0:
            # Determine how many bytes this UTF-8 character has
            while mask & num:
                num_bytes += 1
                mask >>= 1

            # 1 byte characters
            if num_bytes == 0:
                continue
            # Invalid scenarios according to the problem statement
            if num_bytes == 1 or num_bytes > 4:
                return False
        else:
            # If this byte is a part of an existing UTF-8 character,
            # the most significant two bits should be 10.
            if not (num & mask1 and not (num & mask2)):
                return False
        num_bytes -= 1

    # This is for the case where the last UTF-8 character might have been cut off
    return num_bytes == 0
