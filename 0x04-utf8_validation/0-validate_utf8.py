#!/usr/bin/python3

# 0-validate_utf8.py

def validUTF8(data):
    # Number of bytes remaining in the current UTF-8 character
    num_bytes = 0
    
    # Masks to check the start byte and continuation bytes
    mask1 = 1 << 7  # 10000000
    mask2 = 1 << 6  # 01000000

    for byte in data:
        # We only need to consider the 8 least significant bits of each integer
        byte = byte & 0xFF

        if num_bytes == 0:
            # Determine the number of bytes in the UTF-8 character
            if (byte >> 5) == 0b110:  # 2-byte character
                num_bytes = 1
            elif (byte >> 4) == 0b1110:  # 3-byte character
                num_bytes = 2
            elif (byte >> 3) == 0b11110:  # 4-byte character
                num_bytes = 3
            elif (byte >> 7):  # Invalid 1-byte character (should be 0xxxxxxx)
                return False
        else:
            # Check if it's a valid continuation byte (10xxxxxx)
            if not (byte & mask1 and not (byte & mask2)):
                return False
            num_bytes -= 1

    # All characters should be complete (num_bytes should be 0)
    return num_bytes == 0

