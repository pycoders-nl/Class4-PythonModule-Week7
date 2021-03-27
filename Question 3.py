"""
Write a program that list according to email addresses without email domains in a text.
Input: The advencements in biomarine studies franky@google.com
with the investments necessary and Davos sinatra123@yahoo.com.
Then New Yorker article on wind farms...

Output : franky sinatra123
"""
import re


def detect_email(text):
    pattern = "(\w+)@"
    return re.findall(pattern, text)

text = "The advencements in biomarine studies franky@google.com with the investments necessary and " \
       "Davos sinatra123@yahoo.com. Then New Yorker article on wind farms..."

print( "Email addresses without email domains in the text : {}".format(detect_email(text)))
