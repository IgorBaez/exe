class produto:
    def __init__(self,nome,preco):
        self.nome=nome
        self.preco=preco
    def desconto(self):
        Vdesconto=0.09
        valorFinal=self.preco-(self.preco*Vdesconto)
        return valorFinal
       
    
produto1=produto("banana",3.92)
produto2=produto("maçã",4.72)
print("Valor do item com desconto:", produto1.desconto())
print("Valor do item com desconto:",produto2.desconto())


