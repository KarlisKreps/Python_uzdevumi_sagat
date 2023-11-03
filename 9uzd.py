"""
Uzdevumā izmantot funkciju map(), kura  komandu izpilda 
katram saraksta(virknes) loceklim.

"""


skaitli=[1,3,5,67,44,25]
reizinajums=[]

def reizinat(reizinatajs):
    if reizinatajs > 0 and reizinatajs < 5:
        return 2 * reizinatajs

    if reizinatajs > 4:
        return 4 * reizinatajs
    
    if reizinatajs > 40:
        return 20 * reizinatajs

reizinajums = list(map(reizinat,skaitli))
print(reizinajums)