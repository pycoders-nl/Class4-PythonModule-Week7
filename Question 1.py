"""
Write a program that detects the ID number hidden in a text.
We know that the format of the ID number is 2 letters, 1 digit, 2 letters, 2 digits, 1 letter, 1 digit (For example: AA4ZA11B1).
Input   : AABZA1111AEGTV5YH678MK4FM53B6
Output  : MK4FM53B6
Input   : AEGTV5VZ4PF94B6YH678
Output  : VZ4PF94B6
"""
import re

def detect_ID(text):
    pattern = r"\w\w\d\w\w\d\d\w\d"
    for match in re.findall(pattern, text):
        return match


text1 = "AABZA1111AEGTV5YH678MK4FM53B6"
text2 = "AEGTV5VZ4PF94B6YH678"
print( "Searched Text is  : {}\nDetected ID is    : {}".format(text1,detect_ID(text1)))
print(f"Searched Text is  : {text2} \nDetected ID is    : {detect_ID(text2)}")