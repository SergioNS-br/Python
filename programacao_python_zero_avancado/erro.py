try:
    a = 10
    b = 0
    print (a/b)
except ZeroDivisionError:
    print('Divisão NÃO realizada')
else:
    print('Divisão realizada')
finally: # sempre é executado
    print('Calculo concluído')

print('Continua ...')