import re

string = 'The advencements in biomarine studies franky@google.com with the investments necessary and Davos sinatra123@yahoo.com. Then New Yorker article on wind farms...'

pattern = '([\w\d]+)@[\w\d]+'

result = re.findall(pattern, string)

for i in re.findall(pattern, string):
  print (i)