from src.ContaBancaria import ContaBancaria
from src.ContaPoupanca import ContaPoupanca


if __name__=="__main__":
    c = ContaPoupanca()
    c.setNome("Anderson Simplicio")
    c.depositar(10.0)# Realiza deposito de R$ 5,00
    print(c)
    #c.sacar(5.0) #Realiza a retirada de R$ 5,00
    #print(c)
    c.calcularNovoSaldo(0.02)
    print(c)