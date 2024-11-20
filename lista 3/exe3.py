class Carro:
    def __init__(self,modelo,ano):
        self.modelo=modelo
        self.ano=ano
    def __str__(self):
        print('modelo:',self.modelo,'\nano:',self.ano)
    
pessoa1=Carro("uno","2001")
pessoa1.__str__()
