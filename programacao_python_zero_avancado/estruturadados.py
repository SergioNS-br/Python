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

'''
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