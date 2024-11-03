#!/usr/bin/python3
"""
Main file for testing
"""

validUTF8 = __import__('0-validate_utf8').validUTF8

# Test cases
data1 = [65]
print(validUTF8(data1))  # Expected output: True

data2 = [80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 99, 111, 111, 108, 33]
print(validUTF8(data2))  # Expected output: True

data3 = [229, 65, 127, 256]  # 256 is out of 8-bit range; should be converted with & 0xFF
print(validUTF8(data3))  # Expected output: False

# Additional edge cases
data4 = [197, 130, 1]  # Valid 2-byte character followed by a 1-byte character
print(validUTF8(data4))  # Expected output: True

data5 = [235, 140, 4]  # Invalid 3-byte sequence (last byte is incorrect)
print(validUTF8(data5))  # Expected output: False

data6 = [240, 162, 138, 147]  # Valid 4-byte sequence
print(validUTF8(data6))  # Expected output: True

data7 = [250, 145, 145, 145, 145]  # Invalid 5-byte sequence (UTF-8 allows up to 4 bytes)
print(validUTF8(data7))  # Expected output: False

