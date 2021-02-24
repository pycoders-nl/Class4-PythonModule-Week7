        '''Find words that are 8 letter long on this text ;'''

import re
with open('letter8.txt','r') as let_8: #open file with read mode. and assigmented let_8
    type=let_8.read()    
    patern=r"\w{8}" #creaated patern
    for result in re.findall(patern,type):
        print(f'{result}')
    
    
#################################################
print()                                         #
a="Sharp"                                       #        
print(('*'*(50)).center(50))                    #
print(f'Look {a}, Act {a}, Be {a}'.center(15))  #
print('E.Cinar.'.center(60))                    #
#################################################   