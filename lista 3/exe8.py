class CalculadoraSimples:
    def __init__(self,valor1,valor2 ):
        self.valor1=valor1
        self.valor2=valor2
    def soma(self):
        valor=self.valor1+self.valor2
        print("Os valores somados e :",valor)
    def subt(self):
        valor=self.valor1-self.valor2
        print("Os valores subtraidos e :",valor)
numeros=CalculadoraSimples(15,10)
numeros.soma()
numeros.subt()
