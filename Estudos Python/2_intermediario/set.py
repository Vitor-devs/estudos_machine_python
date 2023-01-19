# Sets - Conjuntos em Python (tipo set)
# Conjuntos são ensinados na matemática
# https://brasilescola.uol.com.br/matematica/conjunto.htm
# Representados graficamente pelo diagrama de Venn
# Sets em Python são mutáveis, porém aceitam apenas
# tipos imutáveis como valor interno.

# Sets são eficientes para remover valores duplicados
# de iteráveis.
# - Não aceitam valores mutáveis;
# - Seus valores serão sempre únicos;
# - não tem índexes;
# - não garantem ordem;
# - são iteráveis (for, in, not in)



# Operadores úteis:
# união | união (union) - Une
# intersecção & (intersection) - Itens presentes em ambos
# diferença - Itens presentes apenas no set da esquerda
# diferença simétrica ^ - Itens que não estão em ambos


#Parecem dicionarios, mas não possuem chave e valor
s1 = set({'luiz',2,3})
s2 = set('vitor')
s3 = set()
s3 = {"Vitor", 123}
s4 = set({1,2,2,3,3,3,4,4,4,4,1})
l1 = [1,1,2,2,3,4,5]
s5 = set(l1)
l1 = s5
s6 = set(((3),6,5))
s6 = set([[3],6,5])
s6 = set({{3},6,5}) #Não aceita tipo mutavel

for item in s4:
    print(item)

s1
s2
s3
s4
s5

# Métodos úteis:
# add, update, clear, discard
s1.add("Arroz")
s1.add(5)
s1.update("azul")
s1.update(("verde",15))
s1.update(('Olá mundo', 1, 2, 3, 4))
s1.clear()
s1.discard("a")
s1.discard("z")
s1.discard("u")
s1.discard("l")
s1


# Operadores úteis:
# união | união (union) - Une
# intersecção & (intersection) - Itens presentes em ambos
# diferença - Itens presentes apenas no set da esquerda
# diferença simétrica ^ - Itens que não estão em ambos

set1 = set()
set1 = {1,2,3}

set2 = set()
set2 = {2,3,4}

#Junta os dois
set3 = set1 | set2
set3

#Pega só o que é comum aos dois
set3 = set1 & set2
set3

#Pega só o que for exclusivo da esquerda
set3 = set1 - set2
set3

set3 = set2 - set1
set3

#Itens que não estão presente em ambos
set3 = set1^set2
set3





