# count é um iterador sem fim (itertools)
# não para
from itertools import count

c1 = count(step=8, start=8)
r1 = range(8, 100, 8)
contador = count()

for num in c1:
    #loop infinito
    print(c1)