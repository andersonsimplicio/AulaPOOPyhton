from .ContaBancaria import ContaBancaria
from datetime import date

class ContaPoupanca(ContaBancaria):
   
    def __init__(self)-> None:
        super().__init__()
        self.__data_criacao = date.today().strftime("%d/%m/%Y")
        self.__diaRendimento:int = int(self.__data_criacao[0:2])

    def calcularNovoSaldo(self,txa:float=0.0):
        hoje = int(date.today().strftime("%d"))
        if hoje==self.__diaRendimento and isinstance(txa,float):
            saldo_antigo:float = self.saldo
            novo_saldo:float = saldo_antigo * (1+txa)
            self.saldo = novo_saldo 


    def __str__(self):
         return f"Conta Poupanca:{self.numeroConta}\n Saldo: R$ {self.saldo:.2f} \n Data Criação da Conta:{self.__data_criacao} \
         \n Dia Rendimento:{self.__diaRendimento }"
