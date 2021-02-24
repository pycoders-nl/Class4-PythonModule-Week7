print('*'*21)

'''Write a program that detects the ID number hidden in a text. We know that the format of the ID number is 2 letters, 1 digit, 2 letters, 2 digits, 1 letter, 1 digit (For example: AA4ZA11B1).
Input : AABZA1111AEGTV5YH678MK4FM53B6                   Output : MK4FM53B6
Input : AEGTV5VZ4PF94B6YH678                            Output : VZ4PF94B6'''

import re #RegEx import edilir

id_find=input('Enter the txt: ') #enter text

patern=r"\w{2}\d\w{2}\d{2}\w\d" #patern created.two character, one digit two char.two digit,one char,one digit

for match_find in re.findall(patern,(id_find.upper())):#assigment to match_find
    print(match_find)


#################################################
print()                                         #
a="Sharp"                                       #        
print(('*'*(50)).center(50))                    #
print(f'Look {a}, Act {a}, Be {a}'.center(15))  #
print('E.Cinar.'.center(60))                    #
#################################################