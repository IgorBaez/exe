class Livro:
    def __init__(self,titulo,autor):
        self.titulo=titulo
        self.autor=autor
    def exibir(self):
        print('Título:', self.titulo)
        print('autor:', self.autor)
livro=Livro("a partida dos q nunca chegaram","baz")
livro1=Livro("a volta dos q nao foram",'baz')
livro.exibir()
livro1.exibir()




