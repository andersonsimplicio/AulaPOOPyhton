from faker import Faker

fake = Faker(['pt-br'])
import random

def factory():
    CURSO = [
    "Engenharia de Software",
    "Cientista de Dados",
    "Programador Web",
    "Programador HTML SQN"
    ]

    TURMA =[
        "0012-2021",
        "0013-2021",
        "0014-2021",
        "0015-2021"
    ]

    troca = ['','_','.',random.randint(1, 40)]
    lista_pessoas = []
    for i in range(50):
        nome =fake.name()
        pessoas = {
                "nome":nome,
                "endereco":fake.address(),
                "email":f"{nome}@{fake.email().split('@')[1]}".replace(' ',random.choice(troca).__str__()).lower(),
                "cpf":fake.cpf(),
                "Curso":random.choice(CURSO),
                "Turma":random.choice(TURMA),
                }
        lista_pessoas.append(pessoas)
    return lista_pessoas