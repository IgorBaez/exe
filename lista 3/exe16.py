class Pessoa:
    def __init__(self,nome):
        self.nome=nome
    def cumprimento(self):
        print("Olá Sr/a",self.nome)
eu=Pessoa("baz")
vc=Pessoa("igor")
eu.cumprimento()
vc.cumprimento()
