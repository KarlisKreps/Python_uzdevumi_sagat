"""
Uzrakstiet Python programmu, lai diviem sarakstiem noteikti atšķirību.
Izmantojiet funkciju map().
"""

saraksts1 = [1,2,3,4,5]
saraksts2 = [3,4,5,6,7]

def atslega(skaitlis1, skaitlis2):
    return skaitlis1-skaitlis2

atskiribas_saraksts = list(map(atslega, saraksts1,saraksts2))
print(atskiribas_saraksts)