"""
Papildināt programmu ar ciklu, kurā sarakstā esošiem uzvārdiem tiktu 
pievienots klāt doktora nosaukums - Dr.
"""




saraksts1=["Kalniņš", "Opmanis", "Vēzis", "Almane"]
saraksts2=[]

def pievienot_doktora_nosaukumu(uzvards):
    return "Dr. " + uzvards

saraksts2 = list(map(pievienot_doktora_nosaukumu,saraksts1))
print(saraksts2)