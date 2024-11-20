class Pessoa:
    def __init__(self,nome,idade):
        self.nome=nome
        self.idade=idade
    

    def exibir(self):
        print('nome:',self.nome,'\nidade:',self.idade)
        
pessoa1=Pessoa("baz",23)
pessoa1.exibir()
