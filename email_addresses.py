import re
metin = """ 
        The advencements in biomarine studies franky@google.com with the investments
        necessary and Davos sinatra123@yahoo.com Then New Yorker article on wind farms...
        """
liste = metin.split()
for i in liste:
  sonuc = re.search("(\w+).+com.?$",i)
  if sonuc:
    print(sonuc.group(1))

