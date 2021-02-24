'''Write a program that list according to email addresses without email domains in a text.
Example:
Input   :The advencements in biomarine studies franky@google.com with the investments necessary and Davos sinatra123@yahoo.com. 
         Then New Yorker article on wind farms...
Output  :  franky              sinatra123'''

import re #RegEx import edilir

et='The advencements in biomarine studies franky@google.com with the investments necessary and Davos sinatra123@yahoo.com.'

patern=r"\w+[@]"  #karakter ile baslayan ve @ ile biten patern olusturulur.
nummer=0           #bulunan sonuclari numaralandirmak icin;
for i in re.findall(patern,et): #findall methodu ile bulunan string i atanir
    nummer+=1   
    i=i.strip('@') #stringde bulunan @ karakteri strip kullanilarak cikartilir
    print(f'{nummer}.{i}') 
    
    
#################################################
print()                                         #
a="Sharp"                                       #        
print(('*'*(50)).center(50))                    #
print(f'Look {a}, Act {a}, Be {a}'.center(15))  #
print('E.Cinar.'.center(60))                    #
#################################################