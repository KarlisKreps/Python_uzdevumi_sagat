"""
Uzrakstiet Python programmu, lai trīskāršotu visus dotā veselo skaitļu saraksta skaitļus.
Izmantojiet Python map() funkciju.
"""

skaitlu_saraksts=[1,2,3,4,5,6,7,8]
reizinajums=[]

def reizinat(cipars):
    if isinstance(cipars, int):
        return cipars * 3
    else:
        return cipars

reizinajums = list(map(reizinat,skaitlu_saraksts))
print(reizinajums)