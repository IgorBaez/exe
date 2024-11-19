class Livro:
    def __init__(self,titulo,autor):
        self.titulo=titulo
        self.autor=autor
    def __str__(self):
        return f'nome:{self.titulo} idade:{self.autor}'
        
pessoa1=Livro("baz","rogui")
print(pessoa1.__str__())




