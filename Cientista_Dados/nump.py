import numpy as np
# Criando um numpy array unidimensional
# com o dtype vc pode manipular eles 
mt = np.array([3,2,5,8], dtype=np.float64)
mt
type(mt)

mt2 = np.array([3,2,5,8], dtype=np.int32)
mt2
type(mt2)

array = np.array([3.9,0.8,15.2])
array = array.astype(int)
type(array)

#Bidimensional
mtBiD = np.array([[1,2], [3,4]])
mtBiD

#matriz que não é inicializada, mas nao vazia
vazio = np.empty([3,4])
vazio

#cria matriz x por y de zeros
zeros = np.zeros([4,3])
zeros

#Cria matriz x por y com a diagonal principal 
um = np.ones([5,7])
um

#Matriz quadratica com diagonal principal igual a 
diagonal = np.eye(5)
diagonal

#Cria 4 valores randons de 0 a 1
ale = np.random.random(4)
ale

#Cria com val negativo
aleNeg = np.random.randn(5)
aleNeg

#Cria n numeros aleatórios
aleRandom = 10*np.random.random(3)
aleRandom

#Cria matriz random
aleRandom = 10*np.random.random((3,2))
aleRandom

#Gerar numeros aleatorios
# usa uma semente para obter os mesmos numeros aleatorios (random state tipo isso)
gnr = np.random.default_rng(1)
gerar = gnr.random(3)
gerar

# gera até 9 e 3 elementos
gerarInteiros = gnr.integers(9, size=3)
gerarInteiros

#gera uma matrix 3x4 que vai até o 9
gerarInteirosMatriz = gnr.integers(9, size=(3,4))
gerarInteirosMatriz

#tirar duplicados
arrDuplicado = np.array([11,2,45,278,24,127,582,14,1,2,2,2,2,2])
arrDuplicado = np.unique(arrDuplicado)
arrDuplicado

k = np.array([[1,2,3], [4,5,6], [7,8,9]])
#qual array [linha] [coluna]
k
k[0][2]



#mostra o minimo
k.min()
#mostra o maior elemento
k.max()
# mostra a soma
k.sum()
#mostra a media
k.mean()
#mostra desvio padrao
k.std()

#mostra a raiz de cada elemento
np.sqrt(k)

teste = np.array([1,2,3,4,5,6])
teste[0]
teste[0:5]
teste[0:5:2]


matriz = np.array([[2,4,6], [1,3,5]])
matriz
#linha x coluna
matriz[:,0]
matriz[:,1]
matriz[:,2]

matriz[1,:]


#Soma de matrizes
n = np.array([1,5,9])
o = np.array([2,6,4])

n + o

n*o
p = np.array([[1,5,41], [5,51,8]])
n*p

#transpor matriz que vai até 8 que atualmente é 2x4
f = np.arange(8).reshape((2,4))
f
#transpor em uma 4x2
f.T
f.T.shape


#Expressões lógicas
matrizAleatoria = np.random.randn(4,4)
matrizAleatoria

#Da matriz aleatoria, retorne true para os maiores que zero
condMaiorZero = matrizAleatoria > 0
condMaiorZero

#Agora me diga quais os true, e substitua por 1 e os False por -1
z = np.where(condMaiorZero > 0, 1, -1)
z

