'''
Write a program that detects the ID number hidden in a text. We know that the format of the 
ID number is 2 letters, 1 digit, 2 letters, 2 digits, 1 letter, 1 digit (For example: AA4ZA11B1).
AABZA1111AEGTV5YH678MK4FM53B6----->MK4FM53B6
AEGTV5VZ4PF94B6YH678-------------->VZ4PF94B6
Author= Bulent Caliskan  date= 22/02/2021
'''

import re
def get_Id():
    print(((re.findall('\w{2}\d{1}\w{2}\d{2}\w{1}\d{1}',input("enter text? \n"))))[0])
get_Id()