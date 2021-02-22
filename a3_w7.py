'''
#############################################################################################
#*******************************************************************************************#
#           Copyright (c) 2020 pyCoder|semih Corporation;) All rights reserved.            ##
#                                   [Timestamp:20210222]                                   ##
#*******************************************************************************************#
#############################################################################################
'''
# Write a program that list according to email addresses without email domains in a text.
# Example:
# Input: The advencements in biomarine studies franky@google.com with the investments 
# necessary and Davos sinatra123@yahoo.com. Then New Yorker article on wind farms...
# Output :
# franky
# sinatra123

example = '''The advencements in biomarine studies franky@google.com with the 
investments necessary and Davos sinatra123@yahoo.com. Then New Yorker article on wind farms...'''

import re
for i in example.split():
    nesne = re.search("(\w+).+com.?$",i)
    if nesne:
        print(nesne.group(1))
        
        