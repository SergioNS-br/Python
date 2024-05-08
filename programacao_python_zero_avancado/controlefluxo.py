'''
INDICE:
    If
    For
    While
    Operador Ternário
'''

'''
print ("inicio")
valor_1 = input("Entre com o valor 1: ")
valor_2 = input("Entre com o valor 2: ")

if valor_1 > valor_2:
    print (f"valor 1 ({valor_1}) maior que valor 2 ({valor_2})")
elif valor_2 > valor_1:
    print (f"valor 2 ({valor_2}) maior que valor 1 ({valor_1})")
else:
    print (f"valor 1 ({valor_1}) é igual ao valor 2 ({valor_2})")
    print ("-------------------------------------------------")

print ("fim")
'''
'''
a = True
b = True
c = False
d = False

if a and b:
    print ("Ambos são verdadeiros")
else:
    print("Ops 1")

if a and c:
     print("Ops 2")
else:
   print("São diferentes")

if c and d:
    print("Ops 3")
else:
    print("Ambos são falsos")
'''

'''
valor = int(input("Digite valor: "))
#if valor >= 10 and valor <=15:
if 10 <= valor <=15:
    print("Valor entre 10 e 15")
else:
    print("Valor NÃO está entre 10 e 15")
'''

'''
for numero in range (5):
    print(numero)

for numero in range (1,6):
    print(numero)
'''

'''
for letra in ("Sergio NAntes"):
    print(letra)
'''
'''
for tentativa in range (3):
    if tentativa == 1:
        print ("Acertou !!!")
    else:
        print("Errou !!!")
'''

'''
for tentativa in range (3):
    if tentativa < 3:
        print(f" Número sorteado {tentativa}")
        print ("Acertou !!!")
    else:
        print("Errou !!!")
'''

'''
for x in range (3):
    for y in range (3):
        print(f"Coordenada ({x},{y})")
'''

'''
for letra in ("TESTE"):
    print(letra, end="")
'''

'''
valor = 1
while  valor < 10:
    print (f" {valor} ",end="" )
    valor += 1
'''

'''
#operador ternário
x = 3
print ("deu certo") if x==2 else print ("deu errado")
'''