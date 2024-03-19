from Factory import factory
from Classes.Pessoa import Pessoa
from Classes.Professor import Professor
from random import choices

pessoa = factory().pop()

p = Pessoa(pessoa['nome'],pessoa['cpf'],pessoa['email'])
p.setEnderco(pessoa['endereco'])

pessoa2 = choices(factory()).pop()
professor = Professor(pessoa2['nome'],pessoa2['cpf'],pessoa2['email'])
print(p)
print(professor)