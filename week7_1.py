import re

string = 'AABZA1111AEGTV5YH678MK4FM53B6'
pattern = "\w\w\d\w\w\d\d\w\d"

result = re.findall(pattern, string) 
print(result)