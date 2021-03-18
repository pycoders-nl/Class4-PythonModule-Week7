import re

text="The advencements  in biomarine studies    franky@google.com with   the investments    necessary and Davos  sinatra123@yahoo.com. Then New Yorker article on wind farms..."
a=re.findall("(\w+)@", text)
print(a)