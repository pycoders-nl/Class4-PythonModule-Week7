'''
Kerim Sak
Write a program that list according to email addresses without email domains in a text.

Example:

Input:

The advencements in biomarine studies franky@google.com with the investments necessary and Davos sinatra123@yahoo.com. Then New Yorker article on wind farms...

Output :

franky

sinatra123
'''

import re

def find_email():
    entered_text = input("Enter de text: ")
    pattern = '([\w\d]+)@[\w\d]+'
    emails = re.findall(pattern, entered_text)

    return emails

print(find_email())