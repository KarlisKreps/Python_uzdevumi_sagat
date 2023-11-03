"""
Doti divi saraksti.
Izmantojot funkciju map(), izdrukāt abu sarakstu vienādo( sakrīt elementi un to index) elementu summu.
"""

saraksts1 = [1,2,3,4,5]
saraksts2 = [1,2,5,4,7]

def saskaitit_elementus(skaitlis1, skaitlis2, indekss):
    if skaitlis1 == skaitlis2 and saraksts1.index(skaitlis1) == indekss:
        return skaitlis1 + skaitlis2
    else:
        return 0 
    
sasummetie_elementi = list(map(saskaitit_elementus, saraksts1, saraksts2, range(len(saraksts1))))
summa = sum(sasummetie_elementi)
print("Vienado elementu summa:", summa)
                           
    
    