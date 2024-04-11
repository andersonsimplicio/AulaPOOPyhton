from src.ContaBancaria import ContaBancaria




if __name__=="__main__":
    c = ContaBancaria()
    c.setNome("Anderson Simplicio")
    c.depositar(12.5)
    c.sacar(5)
    c.saldo = "-500"
    print(c)