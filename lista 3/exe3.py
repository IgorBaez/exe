class Carro:
    def __init__(self,modelo,ano):
        self.modelo=modelo
        self.ano=ano
    def __str__(self):
        return f'modelo: {self.modelo} ano: {self.ano}'
pessoa1=Carro("uno","2001")
print(pessoa1.__str__())
