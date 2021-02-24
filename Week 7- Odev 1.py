import re

giris =input('Giris Yapiniz...:')

siralama = r"\w{2}\d{1}\w{2}\d{2}\w{1}\d{1}"
re.search(siralama, giris)
for match in re.findall(siralama, giris):
    print(match)
