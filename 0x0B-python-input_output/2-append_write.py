#!/usr/bin/python3
"""This module contains a function that appends a string at the
end of a text file.
"""


def append_write(filename="", text=""):
    """Appends a string at the end of a text file and returns the
    number of characters added.
    Args:
        filename: the file to append.
        text: the text to append.
    """

    with open(filename, mode='a', encoding='utf-8') as f:
        char_count = f.write(text)

    return char_count
