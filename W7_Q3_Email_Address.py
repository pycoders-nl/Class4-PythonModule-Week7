# Write a program that list according to email addresses without email domains in a text.

import re

text = "The advencements in biomarine studies franky@google.com with the investments necessary and Davos " \
      "sinatra123@yahoo.com. Then New Yorker article on wind farms..."

pattern = r"\s\w+@"
re.search(pattern, text)
for match in re.findall(pattern, text):
    print(match.strip('@'))
