#!/usr/bin/python3
""" UTF-8 Validation"""


def validUTF8(data):
    """
    determines if a given data set represents a valid UTF-8 encoding
    """

    bytes_to_process = 0

    for item in data:
        bina_rep = bin(item)[2:].zfill(8)

        if bytes_to_process == 0:
            """
            determine how many bytes to process based on leading bits
            """
            if bina_rep.startswith('0'):
                """ 1-byte character"""
                continue
            elif bina_rep.startswith('110'):
                bytes_to_process = 1
            elif bina_rep.startswith('1110'):
                bytes_to_process = 2
            elif bina_rep.startswith('11110'):
                bytes_to_process = 3
            else:
                return False

        else:
            """ check if the byte is a valid continuation byte"""
            if not bina_rep.startswith('10'):
                return False
            bytes_to_process -= 1

    return bytes_to_process == 0
