class Filme:
    def __init__(self,titulo,duração):
        self.titulo=titulo
        self.duração=duração
    def exibir(self):
        print('Título:', self.titulo)
        print('duração:', self.duração,"minutos")
filme=Filme("O Senhor dos Anéis: A Sociedade do Anel", 178)
filme1=Filme("a volta dos que ficaram",'149')
filme.exibir()
filme1.exibir()


