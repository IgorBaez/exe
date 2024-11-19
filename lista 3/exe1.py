class Pessoa:
    def __init__(self,nome,idade):
        self.nome=nome
        self.idade=idade

    def calculo(self):
        return f'nome:{self.nome}, idade:{self.idade}'
pessoa1=Pessoa("baz",23)
print(pessoa1.calculo())
