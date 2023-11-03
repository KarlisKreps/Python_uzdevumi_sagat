"""
Izmantojot map() funkciju izveidot no diviem sarakstiem saliktnei.


"""

klases = ['a', 'b', 'c', 'd']
skaitli = [1,2,3,4]

saliktenis = list(map(lambda x,y: str(x) + y, skaitli, klases))

print(saliktenis)