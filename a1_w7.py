'''
#############################################################################################
#*******************************************************************************************#
#           Copyright (c) 2020 pyCoder|semih Corporation;) All rights reserved.            ##
#                                   [Timestamp:20210222]                                   ##
#*******************************************************************************************#
#############################################################################################
'''
# Write a program that detects the ID number hidden in a text. 
# We know that the format of the ID number is 2 letters, 1 digit, 2 letters, 2 digits, 1 letter, 1 digit (For example: AA4ZA11B1).
# Input : AABZA1111AEGTV5YH678MK4FM53B6
# Output : MK4FM53B6

# Input : AEGTV5VZ4PF94B6YH678
# Output : VZ4PF94B6

import re
metin = "firstInput: AEGTV5VZ4PF94B6YH678  secondInput: AABZA1111AEGTV5YH678MK4FM53B6"
li = metin.split()
for i in li:   
    nesne = re.search("[A-Z]+\d[A-Z]+\d+[A-Z]\d", i)
    if nesne:
        print("ID number: ", nesne.group())
    
    
