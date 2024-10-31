#!/usr/bin/python3
"""Module for UTF8 Validation"""


def validUTF8(data):
    """For validating utf8 numbers"""
    # Number of bytes remaining in the current UTF-8 character
    bytes_remaining = 0

    for byte in data:
        # Only keep the last 8 bits (1 byte)
        byte = byte & 0xFF

        if bytes_remaining == 0:
            # Determine the number of bytes in the UTF-8 character
            if (byte >> 7) == 0:         # 1-byte character (0xxxxxxx)
                continue
            elif (byte >> 5) == 0b110:   # 2-byte character (110xxxxx)
                bytes_remaining = 1
            elif (byte >> 4) == 0b1110:  # 3-byte character (1110xxxx)
                bytes_remaining = 2
            elif (byte >> 3) == 0b11110:  # 4-byte character (11110xxx)
                bytes_remaining = 3
            else:
                return False
        else:
            # Validate that the current byte is a continuation byte (10xxxxxx)
            if (byte >> 6) != 0b10:
                return False
            bytes_remaining -= 1

    # If all bytes have been consumed properly, bytes_remaining should be zero
    return bytes_remaining == 0
