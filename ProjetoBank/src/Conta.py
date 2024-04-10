from abc import ABC, abstractmethod
from faker import Faker
fake = Faker('pt_BR')


class ContaBancaria(ABC):
    def __init__(self) -> None:
        super().__init__()
        self.__numeroConta:str=fake.aba()
        self.__nomeCliente:str =""
        self.__saldo:float = 0.0
        
  
    def sacar(self)->float:
        ...
    
    def depositar(self)->float:
        ...

    def setNome(self,nome:str)->None:
        if self.__validaNome(nome):
            self.__nomeCliente = nome
        else:
            raise TypeError("Nome inválido")

    def __validaNome(self,nome)->bool:
        nome_completo = nome.split(" ")
        valido=False
        for name in nome_completo:
            if not name.isnumeric() and name.isalpha():
                valido = True
            else:
                valido = False 
                break
        return valido

    def __str__(self) -> str:
        return f"Numero Conta {self.__numeroConta}\n"

