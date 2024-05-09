import math

print (math.factorial(5))

'''
def texto_v6 (**parametros):
    print (parametros)

texto_v6(marca="VW", modelo="GOL", cor="Cinza", placa="xyz1234")
texto_v6(marca="GM", modelo="Onyx", cor="Preto")
'''

'''
def calculadora_v5 (*numeros):
    soma = 0 #é obrigatório inciar a variavél
    for valor in numeros:
        soma += valor
    return (soma)

print (calculadora_v5(3,2,5))
'''
'''
def calculadora_v4(a=0,b=0,c=0):
    return (a+b+c)

print (calculadora_v4(1,7))
'''

'''
def calculadora_v3(a=0,b=0,c=0):
    print(a+b+c)

calculadora_v3(1)
'''

'''
def calculadora_v2(a,b):
    print (a+b)

calculadora_v2(3,4)
'''

'''
def calculadora_v1():
    a = 5
    b = 6
    print(a+b)


calculadora_v1()
'''