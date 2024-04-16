from abc import ABC, abstractmethod
from faker import Faker
fake = Faker('pt_BR')


class Conta(ABC):
    def __init__(self) -> None:
        super().__init__()
        self.__numeroConta:str=fake.aba()
        self.__nomeCliente:str =""
        self.__saldo:float = 0.0
        
    @abstractmethod
    def sacar(self,valor:float)->float:
       pass
   
    @abstractmethod   
    def depositar(self,valor:float)->float:
        pass

    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self,valor):
        if isinstance(valor,float) and valor is not None:
            self.__saldo=valor
            
    @property
    def numeroConta(self)->float:
        return self.__numeroConta
    

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
    @abstractmethod 
    def __str__(self) -> str:
       pass

