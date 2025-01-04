class Pessoa:
    def __init__(self,nome,idade,peso,altura):
        self.nome=nome
        self.idade=idade
        self.peso=peso
        self.altura=altura
    def crescer(self):
        if self.idade<21:
            x=(21-self.idade)*0.05
            print(self.altura+x)
        elif self.idade>20:
            print("infelizmente não cresce mais ")
    def engordar(self,peso):
        self.peso+=peso

pessoa1=Pessoa("baz",10,75,1.35)
pessoa1.crescer()

    
    
    

        