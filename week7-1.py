import re

text="AABZA1111AEGTV5YH678MK4FM53B6"
a=re.findall("\w{2}\d\w{2}\d{2}\w\d", text)[0]
print(a)