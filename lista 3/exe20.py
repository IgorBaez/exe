class Pessoa:
    def __init__(self,altura):
        self.altura=altura
    def verificar(self):
        if self.altura>1.75:
            print("mais alta")
        else:
            print("mais baixa")

x=Pessoa(1.75)
y=Pessoa(1.77)
y.verificar()
x.verificar()