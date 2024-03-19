from .Pessoa import Pessoa


class  Aluno(Pessoa):
    def __init__(self, nome: str, cpf: str, email: str) -> None:
        super().__init__(nome, cpf, email)