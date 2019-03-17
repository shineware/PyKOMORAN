from PyKomoran import *

komoran = Komoran()
print(komoran)
komoran.analyze("① 대한민국은 민주공화국이다. ② 대한민국의 주권은 국민에게 있고, 모든 권력은 국민으로부터 나온다.")
print(komoran.get_nouns())
print(komoran.get_morphes_by_tags(["NNG", "EF", "SF"]))
print(komoran.get_plaint_text())
print(komoran.get_token_list())
print(komoran.get_token_list(flatten=False))
print(komoran.get_list())
