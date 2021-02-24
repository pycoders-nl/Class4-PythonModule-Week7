import re


def identify_id(str):
    return re.findall("\w{2}\d\w{2}\d{2}\w\d", str)[0]


print("Identity Number:", identify_id('AEGTV5VZ4PF94B6YH678'))
print("Identity Number:", identify_id('AABZA1111AEGTV5YH678MK4FM53B6'))
