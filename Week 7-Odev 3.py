
import re
giris=input('Bir metin giriniz...:')
siralama = r"\s\w+@"
re.search(siralama, giris)
for match in re.findall(siralama, giris):
    print(match.strip('@'))


