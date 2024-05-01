'''
INDICE
    Print
    Sting Formatada
    Comentários
    Variáveis
    Input
    SLICE - pegar parte de uma string
    Métodos em string
'''

'''
#Print
print ("\n")
print ("Teste print de Python")
print ("Segundo teste print de Python")

print ("")

curso = "Python"
horas = 40
print("O curso de " + curso + " tem " + str(horas) + " horas no total")

print ("")

curso2 = "AWS"
horas2 = str(40)
print("O curso de " + curso2 + " tem mais que " + horas2 + " horas")
print ("----------------------------------")


#Sting Formatada
print ("\n") 
nome1 = "Sergio"
nome2 = "Nantes"
nome3 = "Souza"

print (f"Seu nome é {nome1} {nome2} de {nome3}")
print ("----------------------------------")


#Comentários
print ("\n") 
print ("Comentário de linha começa com #")
print ("Comentário em bloco começa e termina com 3 aspas simples "'''" texto "'''" ")
print ("----------------------------------")

#Variáveis
print ("\n") 
x = 2 
print (x)

y = "Olá"
print (y)

z = 2.3
print (z)

print ("")

x = str("3")
y = int (2)
z = float (5)
print(x)
print(y)
print(z)
print ("----------------------------------")

#Input
print ("\n")
valor1 = input("Digite um número  ")
valor2 = input("Digite mais um número ")
resultado = int(valor1) + int(valor2)
# saber o tipo da variável
print ("valor1: " + str(type(valor1)))
print ("valor2: " + str(type(valor2)))
print ("resultado: " + str(type(resultado)))
print ("A soma dos 2 números é: " + str(resultado) )
print ("---------------------------------")


#SLICE - pegar parte de uma string
print ("\n")
palavra = "São Paulo"
#index     012345678

#Pegar a letra "P"
print(palavra[4])

#Pegar as letras "São"
print(palavra[:3])

#Pegar as letras "o Pa"
print(palavra[2:6])

#Pegar as letras "u"
print(palavra[-3])

print ("---------------------------------")

'''

#Métodos em string
print ("\n")
palavra = " Texto de exemplo para métodos"

print(palavra)
print(palavra.lower())
print(palavra.upper())
print(palavra.find("é"))
print(palavra.find("exemplo"))
print(palavra.strip())
print(palavra.replace("o","x"))
print(palavra.replace("Texto","Stringão"))

print ("---------------------------------")