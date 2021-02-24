


import re

veri1 = "AABZA1111AEGTV5YH678MK4FM53B6"
#Output = "MK4FM53B6"
veri2 = "AEGTV5VZ4PF94B6YH678"
#Output = "VZ4PF94B6"

pattern = "\w\w\d\w\w\d\d\w\d"

result = re.findall(pattern, veri1)
print (result)







