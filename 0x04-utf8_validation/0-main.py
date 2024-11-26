#!/usr/bin/python3
"""
Main file for testing
"""

validUTF8 = __import__('0-validate_utf8').validUTF8

# Test cases
print(validUTF8([467, 133, 108]))      # Expected output: False
print(validUTF8([240, 188, 128, 167]))  # Expected output: True
print(validUTF8([235, 140]))           # Expected output: False
print(validUTF8([345, 467]))           # Expected output: False
print(validUTF8([250, 145, 145, 145, 145]))  # Expected output: False
print(validUTF8([0, 0, 0, 0, 0, 0]))   # Expected output: True
print(validUTF8([]))                   # Expected output: True (empty dataset is trivially valid)

