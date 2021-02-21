# Write a program that detects the ID number hidden in a text.
# We know that the format of the ID number is:
# 2 letters, 1 digit, 2 letters, 2 digits, 1 letter, 1 digit (For example: AA4ZA11B1).
#
import re

text = "AABZA1111AEGTV5YH678MK4FM53B6"

pattern = r"\w\w\d\w\w\d\d\w\d"
re.search(pattern, text)
for match in re.findall(pattern, text):
    print(match)
