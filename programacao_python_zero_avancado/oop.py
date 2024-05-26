from datetime import datetime

class pessoa:
    nome = 'Jose'
    sobrenome = 'Santos'
    idade = 23

class people:
    def __init__(self, nome, sobrenome, ano_nascimento):
        self.nome = nome
        self.sobrenome = sobrenome
        self.ano_nascimento = ano_nascimento

    def nome_completo(self):
        return self.nome + ' ' + self.sobrenome

    def idade(self):
        ano = datetime.now().year
        return (ano - int(self.ano_nascimento))
    
pes1 = pessoa
peo = people('Pedro','Mariano','2007')

print(pes1.nome)
print(pes1.sobrenome)
print(pes1.idade)

print()

print(peo.nome)
print(peo.sobrenome)
print(peo.ano_nascimento)

print()

print(peo.nome_completo())
print(people.nome_completo(peo))
print(people.idade(peo))
print('..................')