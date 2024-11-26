#!/usr/bin/python3
"""
Module for validating UTF-8 encoding
"""


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.

    Parameters:
    data (List[int]): List of integers representing bytes of data.

    Returns:
    bool: True if data is a valid UTF-8 encoding, else False.
    """
    num_bytes = 0  # Number of bytes remaining in the current UTF-8 character
    mask1 = 1 << 7  # 10000000
    mask2 = 1 << 6  # 01000000

    for byte in data:
        byte = byte & 0xFF  # Consider only the least significant 8 bits

        if num_bytes == 0:
            # Determine the number of bytes in the UTF-8 character
            if (byte >> 5) == 0b110:       # 2-byte character
                num_bytes = 1
            elif (byte >> 4) == 0b1110:    # 3-byte character
                num_bytes = 2
            elif (byte >> 3) == 0b11110:   # 4-byte character
                num_bytes = 3
            elif (byte >> 7):              # Invalid 1-byte character
                return False
        else:
            # Check if it's a valid continuation byte (10xxxxxx)
            if not (byte & mask1 and not (byte & mask2)):
                return False
            num_bytes -= 1

    return num_bytes == 0  # All characters should be complete
