import re


def user_name(text_2):
    # parantezle sadece @'den önceki kısmı almış oluyor
    return re.findall("(\w+)@", text_2)


text_2 = "The advencements in biomarine studies franky@google.com with the investments necessary and " \
         "Davos sinatra123@yahoo.com. Then New Yorker article on wind farms... "
print(*user_name(text_2), sep='\n')
