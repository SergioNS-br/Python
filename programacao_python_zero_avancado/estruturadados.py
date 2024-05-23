# Listas
'''
cidades = ["Sao Paulo", "Guarulhos", "Aruja", "Santa Isabel", "Jacarei", "São Jose", "Caçapava"]
#index         0             1          2            3            4          5           6
print (cidades)

print (cidades[0])
print (cidades[6])

print (cidades[-1])
print (cidades[-7])

#Substituir conteudo de determinado index
cidades [1] = "Tatauba"

#A linha abaixo não inclui um novo index. Existem funções para incluir.
#A linha abaixo da erro
#cidades [7] = "Taubate"

#Incluir um index no final
cidades.append ("Taubate")

#Incluir um index em qualquer posição
cidades.insert(4, "Guararema")

#Remover 
cidades.remove ("Aruja")

#Remover um index em qualquer posicao
cidades.pop (6)
print (cidades)

#Ordenar
cidades.sort()
print (cidades)


numeros_a = [1, 2, 3, 4, 5]
letras    = ["a","b","c","d","e"]

#Duplica a lista
numeros_b = numeros_a * 2

#Triplica a lista
numeros_c = numeros_a * 3

print(numeros_b)
print(numeros_c)

resultado_1 = numeros_b + letras
#outra forma
numeros_b.extend(letras)
print(resultado_1)
print("outra forma")
print(numeros_b)


itens = [["Nota1", "Nota2"], ["Nota3", "Nota4"]]
# INDEX          0                   1
print (itens[0])
print (itens[1][0])
print (itens[1][1])



frutas = ["Maça","Banana","Pera","Abacaxi"]

var1, var2, var3, var4 = frutas

print (var1)
print (var2)
print (var3)
print (var4)
print ()

frutas2 = ["Maça","Banana","Pera","Abacaxi","Laranja", "Pessego"]
var11, var21, var31, *restodalista = frutas2

print (var11)
print (var21)
print (var31)
print (*restodalista)
print ()

var11, var21, *meiodalista, var51, var61 = frutas2

print (var11)
print (var21)
print (*meiodalista)
print (var51)
print (var61)


x=0
valores = [120, 135, 157, 433]
for i in valores:
    x += i

print (x)


escolha = input("Digite uma letra:")
letras = ["a", "c", "b", "h"]

if escolha.lower() in letras:
    print ("Acertou !!!!")
else:
    print ("ERRROUUU !!!!")



#Juntas listas - MATRIZ
teste = 'Sergio'
a= (list(teste))
print(a)
print()

item = ('Arroz', 'Feijão', 'Carne')
preco = (40, 55, 190)

resultado = zip(item,preco)

print (list(resultado))



lista_produtos = input("Produtos: ")

lista_final = lista_produtos.split(",")

print (lista_final)

'''


#tuple não pode alterar o conteúdo igual a list
'''
lista_list = ['a','b','c']
lista_tuple = ('a','b','c')

print (lista_list)
print (lista_tuple)
print ()
print (type(lista_list))
print (type(lista_tuple))
'''


#array é mais performatico que lista, não tem tem os mesmos recursos
'''
from array import array
letras = array('u', ['a', 'b'])
print (letras)
'''

#SET não usa index e não aceita valores duplicados
'''
list1 = [1,2,3,4,5]
list2 = [4,5,6,7,8,9,10]

set1 = set(list1)
set2 = set(list2)

print (set1)
print (set2)

#Unir sets
print(set1 | set2)

#diferença entre sets
print(set1 - set2)
print(set2 - set1)

#retirar os duplicadas nas 2 sets
print(set1 ^ set2)

# os duplicados
print(set1 & set2)

print (len(set1))
print (len(set2))
'''
'''
set1 = {1,2,3,4,5}
set2 = {4,5,6,7,8,9,10}

set1.add (6)  #Adiciona o mumero a lista
print (set1)

set1.add (4)  #Não adiciona o mumero a lista porque já existe
print (set1)

set1.update([7,8,9,10]) #atualiza o set
print (set1)

set2.remove(8) # remove do set, mas se não existir da erro
print (set2)

set2.discard(4)  #remove do set, mas se não existit NAO da erro
print (set2)
'''

'''
set1 = {'a','b','c'}
set2 = {'a','d','e'}
set3 = {'c','d','f'}

print (set1.union(set2))
print (set1.difference(set3))
print (set1.intersection(set2))
print (set1.symmetric_difference(set3))
'''

# Dicionário


dicio = {'nome':'Sergio', 'apto':103, 'torre':2}

'''
print(dicio['nome'])
print(dicio['torre'])

dicio ['nome'] = 'None'  # Atualiza a key nome
print (dicio)

dicio.update({'nome':'Pedro', 'apto':11, 'torre':'A'}) # Atualiza mais de uma key
print (dicio)

dicio.update({'endereco':'Rua No Way Out', 'numero':235}) # Insere key
print (dicio)

print(dicio.get ('torre'))  # o get é usado para pegar uma chave, se a chave
print(dicio.get ('cep'))    # não existir na da erro. Retorna None

del dicio['numero']         # remove key
print (dicio)
'''
'''
# LOOP em dicionário
for i in dicio:
    print(i)

print()
for i in dicio.values():
    print(i)

print()
for i in dicio.items():
    print(i)

print ()
for chave, valor in dicio.items():
    print (chave +";"+ str(valor))
'''

'''
dicio2 = {'nome':'Sergio', 'apto':103, 'torre':2, 'carros':['Polo','Classic']}

print(dicio2)
print()
print(dicio2.get('carros'))
'''


#Lambda (função sem nome, varios argumentos e 1 expressão)
'''
calculo = lambda x,y,z: ((x+10)*y)/z
print (calculo(4,2,14))

print()

def calculo2 (x,y,z):
    parcial = lambda y,z: y**z
    parcial2 = parcial(y,z) * x 
    return parcial2

print (calculo2(4,5,2))
'''

#MAP
'''
lista1 = [1,2,3,4]

def multi(x):
        return x * 2

lista2 = map(multi, lista1)

#solução com lambda
lista3 =map(lambda x: x * 3,lista1)

print (list(lista2))
print (list(lista3))
'''

# Filter
# filtrar números maiores que 20
'''
valores = [10, 20, 30, 40, 50, 60]

def remover20 (x):
    return x > 20

print (list(filter(remover20,valores)))
print()

# Solução com lambda
print (list((filter(lambda x: x >20, valores ))))
print()
'''

# List comprehension
# Criar lista a partir de uma existente
# Solução sem list comprehension
'''
frutas1 = ['abacate', 'banana', 'morango', 'kiwi', 'abacaxi']
frutas2 = []

for item in frutas1:
    if 'a' in item:
        frutas2.append(item)

print (frutas2)
print ()

# Solução COM list comprehension
frutas3 = [item for item in frutas1 if 'a' in item]
print (frutas3)
print ()
'''

'''
# List comprehension com números
# Solução sem list 
valores = []
for i in range(7):
    valores.append(i * 10)

print (valores)
print()

# Solução com list
valores1 = [i * 10 for i in range(7)]
print (valores1)
'''

#Generator Expressions
#consome menos memória
from sys import getsizeof

# solução sem generator expressions
numeros1 = [x * 1 for x in range(100000000)]
print(type(numeros1))
print (getsizeof(numeros1))
print ()

# solução com generator expressions
numeros2 = (x * 1 for x in range(100000000))
print(type(numeros2))
print (getsizeof(numeros2))