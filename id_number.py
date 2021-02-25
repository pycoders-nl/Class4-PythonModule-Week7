import re
hidden_text= "AEGTV5VZ4PF94B6YH678,AABZA1111AEGTV5YH678MK4FM53B6"
for i in hidden_text.split():
    id_number = re.findall("[A-Z]+\d[A-Z]+\d+[A-Z]\d",i)
    if id_number:
        print(id_number)








