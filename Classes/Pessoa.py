

class Pessoa:

    def __init__(self,nome:str,cpf:str,email:str) ->None:
        self.__Nome:str =  nome
        self.__Cpf:str =  cpf
        self.__Email:str =  email
        self.__Endereco:str = ""
    
    def setEnderco(self,endereco:str):
        self.__Endereco = endereco
    def __str__(self) -> str:
        return f"{self.__Nome} {self.__Email} :ENDERECO: {self.__Endereco}"
