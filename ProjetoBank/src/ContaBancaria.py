from .Conta import Conta


class ContaBancaria(Conta):
    def __init__(self) -> None:
        super().__init__()
    
    
    def sacar(self,valor:float)->float:
        if self.saldo > valor:
            self.saldo = self.saldo-valor
            return valor
        else:
            raise Exception("Saldo Insuficiênte!")

   
    def depositar(self,valor:float)->None:
        if isinstance(valor,float) and valor is not None:
            if valor > 0:
                self.saldo+=valor

    def __str__(self) -> str:
        return f"Numero Conta {self.numeroConta}\nSaldo: R$ {self.saldo:.2f} "