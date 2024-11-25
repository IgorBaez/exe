class Pessoa:
    def __init__(self,nome,idade,peso,altura):
        self.nome=nome
        self.idade=idade
        self.peso=peso
        self.altura=altura
    def envelhecer(self):
        if self.idade<21:
            x=(21-self.idade)*0.05
            print(self.altura+x)
        elif self.idade>20:
            print("infelizmente não cresce mais ")

pessoa1=Pessoa("baz",21,75,1.35)
pessoa1.envelhecer()

    
    
    

        