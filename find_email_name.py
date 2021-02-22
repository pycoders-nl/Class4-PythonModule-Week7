'''
Write a program that list according to email addresses without email domains in a text.

Author= Bulent Caliskan  date= 22/02/2021
input=The advencements in biomarine studies franky@google.com with the investments necessary and Davos sinatra123@yahoo.com. Then New Yorker article on wind farms...
output=  franky
         sinatra123
'''
import re

def find_email_name():
    print(*(i for i in (re.findall('(\S+)@' ,input("enter text?\n ")))),sep='\n')

find_email_name()    