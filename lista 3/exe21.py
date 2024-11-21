class Livro:
    def __init__(self, titulo, autor, estoque):
        self.titulo = titulo  
        self.autor = autor
        self.estoque = estoque 

    def verificar_estoque(self):
        return self.estoque
    
    def vender_livro(self, quantidade=1):
        if self.estoque >= quantidade:
            self.estoque -= quantidade
            print(quantidade,' livro(s) de ',self.titulo,' vendido(s). Estoque restante:',self.estoque)
        else:
            print(f"Estoque insuficiente para vender {quantidade} livro(s). Estoque atual: {self.estoque}.")

livro1 = Livro("O Senhor dos Anéis", "J.R.R. Tolkien", 10)
print('Estoque de ',livro1.titulo,':',livro1.verificar_estoque())

livro1.vender_livro(3)
livro1.vender_livro(8) 
