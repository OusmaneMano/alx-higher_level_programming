#!/usr/bin/python3
"""print the alphabet in lowercase, not followed by a new line"""
for letter in range(97, 123):
    print(chr(letter).format(), end="")
