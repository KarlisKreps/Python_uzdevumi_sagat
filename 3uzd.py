"""
Uzrakstiet programmu, izveidot klasi ar nosaukumu
Dati. Izveidot objektu, kas inicializētu atribūtus, 
piemēram, vārdu, vecumu un ceļojumam iemaksāto summu.

"""

class Dati:
    def __init__(self, vards,vecums,iemaksata_summa):
        self.vards = vards
        self.vecums = vecums
        self.iemaksata_summa = iemaksata_summa

mani_dati = Dati("Janis", 30, 500)